'''
Created on Mar 29, 2012

@author: gsinghal
'''

import re, sys

def count_size(filename):

    fh = open(filename, 'rU')

    total_size = []

    data = fh.readlines()
    for line in data:
        size = line.split(',')[1].strip()
        if re.search('GB', size):
            fs = float(size[:-2])*1024
        elif re.search('kB', size):
            fs = float(size[:-2])/1024

        else:
            fs = float(size[:-2])
        total_size.append(fs)

    totalSize = sum(total_size)
    print '# of files in', filename, '= ', len(total_size)
    print ' total size in MB = ',  totalSize
    print 'total size in GB = ', totalSize/1024

#    print total_size[:10]
#    print sum(total_size[:10])

def main():
    filename = sys.argv[1]
    count_size(filename)

if __name__=='__main__':
    main()