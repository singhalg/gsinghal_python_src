'''
Created on Jul 21, 2010

@author: Gaurav
'''
def RECounter(file):
    input = open (file, 'rU')
    
    
    for line in input:
        plist = organize(line)
        #print 'printing line from the input file', plist
        repEl = plist[9]
        
         
            Repeats.append(plist)
            if write:
                output.write(line)
#
#    output = open('w')
        
   
   
   
def organize(string):
    string = string.strip() # stripping the string of the leading and trailing whitespaces
    oldlist = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    list = []
    for word in oldlist:
        list.append(word.strip('()')) #this removes all occurances of ( or ) in the string, and the stripped word is appended to the list
    plist = [int(list[0]), list[1], list[2], list[3], list[4], int(list[5]), int(list[6]), int(list[7]), list[8], list[9], list[10], int(list[11]), int(list[12]), int(list[13]), int(list[14])]
    
    
    #plist = processed list, all the string that can be converted into int are being converted here.
    return plist 