import subprocess
import sys

bowtie_dir =  '/net/artemis/mnt/work2/seqApps/bowtie-0.12.7/'
shortfuse_dir = '/net/artemis/mnt/work1/projects/gsinghalWork/GSseqApps/ShortFuse/'
offset = '33'


EM_bin = shortfuse_dir + 'EmFusion'
bowtie_bin = bowtie_dir + 'bowtie'
bowtie_build_bin = bowtie_dir + 'bowtie-build'

exon_structure_file = shortfuse_dir + 'ref/refseq_exon_structure.txt'
exon_seq_file = shortfuse_dir + 'ref/exon_seqs_refseq.fa'

initial_bowtie_flags = '-l 35 -e 150 -n 2 -a -m 150 -p 10 '
discord_bowtie_flags = '-l 22 -e 350 -n 3 -y -a -m 5000 -p 10 '
pe_bowtie_flags = '-a -p 10 -X 2000 -m 1500 --chunkmbs 1024 '

chrom_regions = shortfuse_dir + 'ref/chrom_regions.txt'
transcripts_plus_genome = shortfuse_dir + 'ref/transcripts_plus_genome'
reference_root = shortfuse_dir + 'ref/refseq_transcripts'
reference_fasta = shortfuse_dir + 'ref/RefSeqTranscripts_50up_polyA.fasta'

def main(fastq1, fastq2):


    p = subprocess.Popen(' '.join([bowtie_bin, initial_bowtie_flags, '--max 1.repeat',
                                  reference_root, fastq1, fastq1 + '.bowtie']), shell = True)
    p.wait()
    p = subprocess.Popen(' '.join([bowtie_bin, initial_bowtie_flags, '--max 2.repeat',
                                  reference_root, fastq2, fastq2 + '.bowtie']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'bowtie', fastq1 + '.bowtie']), shell = True)
    p.wait()
    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'bowtie', fastq2 + '.bowtie']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'fasta', '1.repeat']), shell = True)
    p.wait()
    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'fasta', '2.repeat']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'fastq', fastq1]), shell = True)
    p.wait()
    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'fastq', fastq2]), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join([EM_bin, 'sift', fastq1 + '.bowtie', fastq2 + '.bowtie',
                                  fastq1, fastq2, offset, '1.repeat', '2.repeat']),
                                   shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['sort -k 2,2 -k 3,3', fastq1 + '.discord', '>',
                                   fastq1 + '.discord.sorted']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join([bowtie_bin, discord_bowtie_flags, '--max',
                                  fastq1 + '.discord.fastq.bust', transcripts_plus_genome,
                                  fastq1 + '.discord.fastq', 'concordant.bt']),
                                  shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'fa2ridlist.py',
                                   fastq1 + '.discord.fastq.bust', '>',
                                   'concordant.reads']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'parseBowtie.py',
                                   'concordant.bt', chrom_regions, '100', '>>',
                                   'concordant.reads']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'ExtendReference.py',
                                   exon_structure_file, fastq1 + '.discord.sorted', 'concordant.reads']),
                                   shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['sort -k 2 -u', fastq1 + '.discord.sorted.exons',
                                   '>', fastq1 + '.discord.sorted.exons.uniq']),
                                    shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'MakeFusionTranscripts.py',
                                    exon_seq_file, fastq1 + '.discord.sorted.exons.uniq']),
                                    shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['cat', fastq1 + '.discord.sorted.exons.uniq.seqs',
                                   reference_fasta, '>', 'augmented_ref.fa']),
                                    shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['rm', fastq1 + '.bowtie', fastq2 + '.bowtie']),
                            shell = True)
    p.wait()

    p = subprocess.Popen(' '.join([bowtie_build_bin, '-o 0', 'augmented_ref.fa',
                                   'augmented_ref']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join([bowtie_bin, pe_bowtie_flags,
                                   'augmented_ref', '-1', fastq1, '-2', fastq2,
                                    fastq1 + '.pe.bowtie']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'PythonSort.py',
                                   'paired_bowtie', fastq1 + '.pe.bowtie']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['sort -n -k 1,1', fastq1 + '.mapdist', '>',
                                   fastq1 + '.mapdist.sorted']), shell = True)
    p.wait()

    p = subprocess.Popen(' '.join(['python', shortfuse_dir + 'getdistprob.py',
                                   fastq1 + '.mapdist.sorted', 'dist.prob']),
                                   shell = True)
    p.wait()

    p = subprocess.Popen(' '.join([EM_bin, 'EM', fastq1 + '.pe.bowtie', 'dist.prob',
                                   'augmented_ref.fa', offset]), shell = True)
    p.wait()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python run_pipeline.py <fastq1> <fastq2>"
        sys.exit()
    main(*sys.argv[1:])


