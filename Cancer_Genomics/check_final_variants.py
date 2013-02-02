#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     24/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys
from sets import Set

def checkValidatedVariants(all_variants_file, finally_validated_file):
    all_variants = Set()
    validated = Set()

    all_data = open(all_variants_file, 'rU').readlines()
    for line in all_data[1:]:
        flds = line.strip().split(',')
        pos = flds[0] + '#' + flds[1]
        all_variants.add(pos)

    selected = open(finally_validated_file, 'rU').readlines()
    for line in selected[1:]:
        flds = line.strip().split(',')
        pos = flds[0] + '#' + flds[1]
        validated.add(pos)
##    print all_variants
##
##    print validated

    print '# of all variants = ', len(all_variants)

    print '# of validated variants = ', len(validated)

    print '# of validated variants that were not present in all_variants = ', (len(validated - all_variants))

    print len(all_variants - validated)

    print (validated - all_variants)

def main():
    all_variants = sys.argv[1]
    finally_validated = sys.argv[2]
    checkValidatedVariants(all_variants, finally_validated)

if __name__ == '__main__':
    main()
