#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     09/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import datetime
def printX():
    st = time.time()

    time.sleep(11)

    e = (time.time() - st)



    print 'it took ', e, ' minutes'
    print  ' it took ', str(datetime.timedelta(seconds=e))

def main():
    printX()

if __name__ == '__main__':
    main()
