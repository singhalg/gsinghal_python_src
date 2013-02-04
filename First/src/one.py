# this is a comment

a = 'a simple string';
b = 5;
print a;
print b;


job = ' to parse the file, extracting gene name, chromosome number, strand and coordinates';

import sys
if len(sys.argv) != 2:
    print 'Require input file'
    sys.exit()
    
with open(sys.argv[1]) as fin:
    for line in fin:
        lst = line.rstrip().split('\t')
        print '{0[0]}\t{0[2]}:{0[4]}-{0[5]}'.format(lst)