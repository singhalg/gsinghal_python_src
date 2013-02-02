#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     15/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle

def recurrentInCosmic(file_name):

    fh = open(file_name, 'rU')
    data = fh.readlines()
    fh.close()
    mut_loc_count = {}
    for line in data[1:]:
        flds = line.split('\t')
        chrom = flds[19].partition(':')[0]
        pos = flds[19].partition('-')[2]
        loc = chrom + '#' + pos
        if loc in mut_loc_count:
            count = mut_loc_count[loc]
            count+=1
            mut_loc_count[loc] = count
        else:
            mut_loc_count[loc] = 1

##    print mut_loc

    fhPickle = open('cosmic_V61_mutations_locations_recurrence.pkl', 'w')
    pickle.dump(mut_loc_count, fhPickle)
    fhPickle.close()

def main():
    recurrentInCosmic('CosmicMutantExport_v61_260912.tsv')

if __name__ == '__main__':
    main()
