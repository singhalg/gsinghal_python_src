'''
Created on May 25, 2010

@author: Gaurav


'''
import sys
import decimal


"""
@param file: The file that needs to be parsed. Usually, this is an output of repeat masker. 
@param : repFamily : string, which is the name of the repeat family
@param : boolean : write : true / false or 0/1 , if true, this method creates a new file and write the output to that file.
return : returns a list of all the lines in the input file that contain repFamily in col[9]
"""

def Parser(file, repFamily, write):
    Repeats = []
    if write: # make a new output stream if write is supplied as True
        output = open(repFamily, 'w')
        
    input = open (file, 'rU')
    #input.readline()    # removing the first 3 lines of the file; these 3 lines do not contain the target info
    #input.readline()
    #input.readline()
    #print input.readline() #just printing the first line of data to ensure that everything is going fine
    for line in input:
        plist = organize(line)
        #print 'printing line from the input file', plist
        if plist[9] == repFamily:
            Repeats.append(plist)
            if write:
                output.write(line)
            
        #else # do nothing, just move on to the next list 
    #just printing first 50 lines of Repeat list
    for line in Repeats[:50]:
        print line
    input.close()
    if write == True:
        output.close()
    return Repeats


"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):
    string = string.strip() # stripping the string of the leading and trailing whitespaces
    oldlist = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    list = []
    for word in oldlist:
        list.append(word.strip('()')) #this removes all occurances of ( or ) in the string, and the stripped word is appended to the list
    plist = [int(list[0]), list[1], list[2], list[3], list[4], int(list[5]), int(list[6]), int(list[7]), list[8], list[9], list[10], int(list[11]), int(list[12]), int(list[13]), int(list[14])]
    #plist = processed list, all the string that can be converted into int are being converted here.
    return plist
    


    

def main():
    openfile = sys.argv[1]
    repFamily = sys.argv[2]
    boolean = sys.argv[3]
    Parser(openfile, repFamily, boolean)   
 



if __name__ == '__main__':
    main()