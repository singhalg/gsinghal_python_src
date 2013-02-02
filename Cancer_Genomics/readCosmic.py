#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     12/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

'''
This method takes in the csv file containing coding point mutations in COSMIC and saves a pickle which contains all the locations of point mutations.
Once we have these locations, we will see if any of the recurrent mutations in our data set is also present in the COSMIC

'''
import pickle, sys
from sets import Set

def readCosmic(cosmicFile):
    fh = open(cosmicFile, 'rU')
    data = fh.readlines()
    fh.close()
    mut_loc = Set([])
    for line in data[1:]:
        flds = line.split(',')
        chrom = flds[19].partition(':')[0]
        pos = flds[19].partition('-')[2]
        loc = chrom + '#' + pos
        mut_loc.add(loc)

##    print mut_loc

    fhPickle = open('cosmic_V60_coding_Point_mutations_locations.pkl', 'w')
    pickle.dump(mut_loc, fhPickle)
    fhPickle.close()


def main():
    readCosmic('CosmicMutantExport_v60_190712.csv')

if __name__ == '__main__':
    main()
