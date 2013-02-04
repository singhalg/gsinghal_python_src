#-------------------------------------------------------------------------------
# Name:        exomeCoverageAnalysis
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     31/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, os
from subprocess import Popen, PIPE, STDOUT

def exonCoverageAnalysis(exon_coordinates_file, exome_coverage_file, output_fileName):
    # convert exon_coding.txt file into bed format
    exon_bedFile = exonFile2Bed(exon_coordinates_file)

    intersectBed = ' intersectBed -a '+ exome_coverage_file + ' -b ' + exon_bedFile + '  -wa -wb > ' + output_fileName+'_.bed ' +'\n'

    intersectBedJob = Popen(intersectBed,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    intersectBedJob.wait()

    intersectBed_V = ' intersectBed -a '+ exome_coverage_file + ' -b ' + exon_bedFile + '  -v > ' + output_fileName+'_no_coverage.bed ' +'\n'

    intersectBedJob_V = Popen(intersectBed_V,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    intersectBedJob_V.wait()

    finalOutput = open(output_fileName, 'w')

    output_data = open(output_fileName+'_.bed', 'rU').readlines()
    finalOutput.write('gene\tchr\texon_id\thq coverage\tposition\tposition2\tin_range\tcoding\ttranscript_acc\n')
    for line in output_data:
        flds = line.strip().split('\t')
        outline = flds[10]+ '\t'+ flds[4] + '\t'+ flds[7]+ '\t' + flds[3] +'\t'+ flds[1]+'\t' + flds[2]+'\t' + 'TRUE'+'\t'+ flds[8]+ flds[9] + '\n'
        finalOutput.write(outline)

    noCoverageData = open(output_fileName+'_no_coverage.bed', 'rU').readlines()
    for line in noCoverageData:
        flds = line.strip().split('\t')
        outline ='NA' + '\t'+ flds[0] + '\t'+ 'NA' + '\t' + flds[3] +'\t'+ flds[1]+'\t' + flds[2]+'\t' + 'FALSE'+'\t'+ 'NA' + 'NA' + '\n'
        finalOutput.write(outline)
    finalOutput.close()

def exonFile2Bed(exon_coordinates_file):
    bedFileName = exon_coordinates_file+'_.bed'
    fhOut = open(bedFileName, 'w')
    data = open(exon_coordinates_file, 'rU').readlines()
    for line in data[1:]: # here we assume that the first line in exon_coordinates_file is the header line
        flds = line.strip().partition('\t')
        outline = flds[2] + flds[1] + flds[0] + '\n'
        fhOut.write(outline)

    fhOut.close()
    return bedFileName



def main():
    exon_coordinates = sys.argv[1]
    exome_coverage_file = sys.argv[2]
    outfile = sys.argv[3]

    exonCoverageAnalysis(exon_coordinates, exome_coverage_file, outfile)

if __name__ == '__main__':
    main()
