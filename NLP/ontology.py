'''
Created on Jan 16, 2012

@author: gsinghal
'''
import sys, re


from sets import Set

def buildOntology(filename):
    fh = open(filename, 'rU')
    data = fh.readlines()
    
    index = {}
        
    for aline in data:
        fields = aline.split('\t')
        code = fields[0]
        name = fields[1]
        parent = fields[2].split('|')
        synonym = fields[3].split('|')
        definition = fields[4]
        index[name] = [parent, synonym, definition ] 
           
            
    
    print len(index)
    itkeys = iter(index)
    cancers = {}
    
    for each in itkeys:
        if (re.search('cancer', each) or re.search('tumor', each) or re.search('malignant', each)):
            cancers[each] = index[each] 
    
    print len(cancers)
    
    cn =  iter(cancers)
    for aCancer in cn:
        print aCancer
        print cancers[aCancer]
    
def main():
    filename = sys.argv[1]
    buildOntology(filename)
    

if __name__=='__main__':
    main()