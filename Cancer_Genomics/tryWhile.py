#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     24/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import random

def tryWhile():
    for i in range(10):

        loc_depth = {4:'abc', 2:'dbd', 3:'cdc'}
        max_iters = 5
        while max_iters>0:
            max_iters-=1
            baseLoc = random.randint(2, 20)


            if baseLoc in loc_depth:
                break
            else:
                print 'Attempt ', i, ' : ', baseLoc, 'is not a key'
        print 'Failed to find a key'

        print 'Attempt ', i, '. : Key ', baseLoc, ' found. Value = ', loc_depth[baseLoc]



def main():
    tryWhile()

if __name__ == '__main__':
    main()
