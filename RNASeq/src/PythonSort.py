#!/usr/bin/python

from heapq import heappop, heappush
from itertools import islice, cycle
from tempfile import gettempdir
import os
import re
import subprocess
import sys
import tempfile

FASTQ = False

fastq_re = r'@.+\n[ACTGN]+\n\+.*\n.+\n'
fasta_re = r'>(.+\n)(\S+\n(?!>))*(\S+\n(?=(\n*>|\n*$$)))'

def merge(chunks,key=None):
    if key is None:
        key = lambda x : x

    values = []

    for index, chunk in enumerate(chunks):
        try:
            iterator = iter(chunk)
            value = iterator.next()
        except StopIteration:
            try:
                chunk.file.close()
                #os.remove(chunk.file.name)
                chunks.remove(chunk)
            except:
                pass
        else:
            heappush(values,((key(value),index,value,iterator,chunk)))

    while values:
        k, index, value, iterator, chunk = heappop(values)
        yield value
        try:
            value = iterator.next()
        except StopIteration:
            try:
                chunk.file.close()
                os.remove(chunk.file.name)
                chunks.remove(chunk)
            except:
                pass
        else:
            heappush(values,(key(value),index,value,iterator,chunk))

def batch_sort(input,output,key=None,buffer_size=1048576,tempdirs=['./'], re_pattern = '.*\n'):
    if not tempdirs:
        tempdirs.append(gettempdir())
    #tdir = os.tempnam(tempdirs[0])
    tdir = tempfile.mkdtemp(dir=tempdirs[0], prefix = 'sort')
    #os.mkdir(tdir)
    
    input_file = multi_file(input, mode = 'rb', re_pattern = re_pattern)
    try:
        input_iterator = iter(input_file)
        
        chunks = []
        try:
            for tempdir in cycle([tdir]):
                current_chunk = list(islice(input_iterator,buffer_size))
                if current_chunk:
                    current_chunk.sort(key=key)
                    output_chunk = multi_file(os.path.join(tempdir,'%06i'%len(chunks)),
                                              mode = 'w+b', re_pattern = re_pattern)
                    output_chunk.file.writelines(current_chunk)
                    output_chunk.file.flush()
                    output_chunk.file.seek(0)
                    chunks.append(output_chunk)
                else:
                    break
        except RuntimeError:
            for chunk in chunks:
                try:
                    chunk.close()
                    os.remove(chunk.name)
                except:
                    pass
            if output_chunk not in chunks:
                try:
                    output_chunk.close()
                    os.remove(output_chunk.name)
                except:
                    pass
            os.rmdir(tdir)
            return
    finally:
        input_file.close()
    
    output_file = file(output,'wb',256 * 1024)
    try:
        output_file.writelines(merge(chunks,key))
    finally:
        for chunk in chunks:
            try:
                chunk.close()
                os.remove(chunk.name)
            except:
                pass
        os.rmdir(tdir)
        output_file.close()
    
class multi_file(file):
    
    def __init__(self, name, mode = 'rU', re_pattern = '.*\n', buffsize = 1024):
        self.file = file(name, mode)
        #print 're_pattern is ' + re_pattern

        self._re_pattern = re.compile(re_pattern)

        self._buffer = ''
        self._buffsize = buffsize
        self._EOF = False
    
    def __iter__(self):
        return self
    
    def _readmore(self):
        nextbytes = self.file.read(self._buffsize)
        if not nextbytes:
            self._EOF = True
        #print nextbytes
        self._buffer += nextbytes
#        if FASTQ and self._EOF:
#            self._buffer += '\n'
    
    def next(self):
        #print 'called next', self._buffer
        m = self._re_pattern.search(self._buffer)
        #print 'searched one'
        
        while not m and not self._EOF:

            self._readmore()

            m = self._re_pattern.search(self._buffer)
        
        if not m and self._EOF:
            raise StopIteration
        
        m_string = m.group(0)
        self._buffer = self._buffer[m.end():]
        
#        if FASTQ and self._EOF and \
#           len(self._buffer) == 0 and \
#           m_string[-1] == '\n':
#            m_string = m_string[:-1]
        
        return m_string
        

if __name__ == '__main__':
    
    if sys.argv[1] == 'fastq':
        FASTQ = True
        fastqfile = sys.argv[2]
        batch_sort(fastqfile, fastqfile + '.tmp', tempdirs=['./'], re_pattern=fastq_re)
        assert os.path.getsize(fastqfile) == os.path.getsize(fastqfile + '.tmp')
        p = subprocess.Popen('wc -l ' + fastqfile, shell = True, stdout = subprocess.PIPE)
        count1 = int(p.communicate()[0].split()[0])
        p = subprocess.Popen('wc -l ' + fastqfile + '.tmp', shell = True, stdout = subprocess.PIPE)
        count2 = int(p.communicate()[0].split()[0])
        assert count1 == count2
        os.remove(fastqfile)
        os.rename(fastqfile + '.tmp', fastqfile)
    elif sys.argv[1] == 'fasta':
        filename = sys.argv[2]
        batch_sort(filename, filename + '.tmp', tempdirs=['./'], re_pattern=fasta_re)
        assert os.path.getsize(filename) == os.path.getsize(filename + '.tmp')
        os.remove(filename)
        os.rename(filename + '.tmp', filename)
    elif sys.argv[1] == 'bowtie':
        filename = sys.argv[2]
        batch_sort(filename, filename + '.tmp', tempdirs=['./'], re_pattern = '.*\n')
        assert os.path.getsize(filename) == os.path.getsize(filename + '.tmp')
        os.remove(filename)
        os.rename(filename + '.tmp', filename)
    elif sys.argv[1] == 'paired_bowtie':
        filename = sys.argv[2]
        batch_sort(filename, filename + '.tmp', tempdirs=['./'], re_pattern = '.*\n.*\n',
                    key = lambda x: x.split('\t')[2])
        assert os.path.getsize(filename) == os.path.getsize(filename + '.tmp')
        os.remove(filename)
        os.rename(filename + '.tmp', filename)
