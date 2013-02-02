#!/usr/bin/env python
'''
Compares two files if we have a coding exon or not.
'''
from __future__ import with_statement

import copy
import glob
import os
import sys

from pprint import pprint as pp
from collections import defaultdict
from csv import DictReader, DictWriter


exon_data = {}
all_bp_data = {}


def read_exon_txt(file):
	'''read in a file and return a dict of { chr: [ {start:x end: y}, ...]'''

	d = defaultdict(list)

	with open(file, 'rU') as f:
		reader = DictReader(f, dialect='excel-tab')
		for row in reader:
			#print "File: %s row: %s " % (file, row)
			if row.has_key('start'):
				startfield = 'start'
				endfield = 'end'
			try:
				d[row['chr']].append( { 'gene': row['gene'], 'start':row[startfield], 'end': row[endfield], 'exon_id':row['exon_id'], 'coding':row['coding'] } )
			except:
				print("Error reading in %s"  % row)
	#pp(d)
	#pp(d.keys())
	return d


def read_bp_txt(file, fieldnames = ['chr', 'position', 'position2', 'hq coverage'] ):
	'''read in a file and return a dict of { gene: [ {start:x end: y}, ...]'''

	with open(file, 'rU') as f:
		reader = DictReader(f, fieldnames=fieldnames, dialect='excel-tab')
		for row in reader:
			try:
				yield row
			except :
				yield {}


def check_data(exons, cds):
	'''check to see if we have a position match for a gene within an exon range.

	For each gene in the cds dictionary, we check if any of the start or end values are within any of the exon value ranges.
	'''

	for k,v in cds.items():
 		for index, data in enumerate(v): #this is an individual line of start, end results

			#print "checking: %s" % k
			res = check_range(data, exons[k])
			cds[k][index].update(res)

		#pp(cds.items())

	#pp(cds.items())
	#pp(exons.items())

def check_range(data, exons, dictWriter):
	'''check an individual gene'''

	result = { 'in_range': 'FALSE',
                'exon_id':'N/A',
                'coding':'N/A'
                }

	for ex in exons[data['chr']]:
		#print "bp_data: %s %s" % (data['start'], data['end'])
		#print "Ex:  %s %s" % (ex['start'], ex['end'])
		if  int(ex['start']) <=  int(data['position']) <= int(data['position2']) <= int(ex['end']):
			#print "Match"
			result['in_range'] = 'TRUE'
			#result['match_info'] = "chr %s within %s and %s" % (data['position'], ex['start'], ex['end'])
			result['exon_id'] = ex['exon_id']
			result['coding'] = ex['coding']
			result['gene'] = ex['gene']

        data.update(result)
	#pp(result)
	#pp(data)
	dictWriter.writerow(data)


def open_output(outfile,headings = ['gene', 'chr', 'exon_id',  'hq coverage', 'position', 'position2', 'in_range', 'coding' ]):
    print "Writing to %s" % outfile
    f = (open(outfile, 'w'))
    writer = DictWriter(f, headings, dialect='excel-tab')

    writer.writerow(dict(zip(headings,headings )))

    return writer

def main():
    #exon_file = 'coding2.txt'
    #all_bp = 'all.bp/all.bp.CTNNB1'

    exon_file = sys.argv[1]
    all_bp = sys.argv[2]
    try:
        outfile = sys.argv[3]
    except:
        outfile = 'output.txt'

    exon_data = read_exon_txt(exon_file)

    print "Processing %s" % all_bp

    #generator for our bp_file
    bp_data = read_bp_txt(all_bp)

    writer = open_output(outfile)

    for line in bp_data:
        check_range(line, exon_data, writer)

if __name__ == '__main__':
	main()

