#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     10/10/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def addTags(input_fileName, output_filename):

    fh = open(input_fileName, 'rU')
    data = fh.readlines()
    fh.close()

    fhout = open(output_filename, 'w')
    all_output = []
    for line in data:

        # Preceeding tag #    # edit here
        preceding_tag = "<value><name>"

        #Succeeding tag #     # edit here
        succeeding_tag = "</name></value>"

        all_output.append( preceding_tag + line.strip() +succeeding_tag + '\n')
    fhout.writelines(all_output)
    fhout.close()



def main():

  # addTags(input_filename, output_filename)

    addTags('Meds.txt', 'Meds_w_text.txt')

if __name__ == '__main__':
    main()
