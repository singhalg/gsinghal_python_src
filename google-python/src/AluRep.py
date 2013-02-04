'''
Created on May 24, 2010

@author: Gaurav
'''
import sys

"""
@param filename:takes in a file to parse its contents
@param param: returns the list of repeats based on this parameter, which can be AluRep, AluSp, AluSx, AluSc, AluSq, AluSg, AluSg1, AluJo, AluJ, AluJb, AluY, AluYa5, AluYa8, AluYb8, AluYb9, AluYc, AluYc3, AluYc5, AluYd8, AluYg6, AluYh9
@return: depending on the param, returns a list of repeats for that family (ALu---) or the entire list (AluRep). 
"""

def AluRep(filename, param):
    AluSp = []
    AluSx = []
    AluSc = []
    AluSq = []
    AluSg = []
    AluSg1 = []
    AluJo = []
    AluJ = []
    AluJb = []
    AluY = []
    AluYa5 = []
    AluYa8 = []
    AluYb8 = []
    AluYb9 = []
    AluYc = []
    AluYc3 = []
    AluYc5 = []
    AluYd8 = []
    AluYg6 = []
    AluYh9 = []
    
    fileData =  open(filename, 'rU')
    for line in fileData:
        list = Find(line)
        if list[3]=='AluSc':
            AluSc.append(list)
        elif list[3] =='AluSp':
            AluSp.append(list)
        elif list[3]=='AluSx':
            AluSx.append(list)
        elif list[3] =='AluSq':
            AluSq.append(list)
        elif list[3] =='AluSg1':
            AluSg1.append(list)
        elif list[3]=='AluJo':
            AluJo.append(list)
        elif list[3] =='AluJ':
            AluJ.append(list)
        elif list[3]=='AluJb':
            AluJb.append(list)
        elif list[3] =='AluY':
            AluY.append(list)
        elif list[3] =='AluYa5':
            AluYa5.append(list)
        elif list[3]=='AluYa8':
            AluYa8.append(list)
        elif list[3] =='AluYb8':
            AluYb8.append(list)
        elif list[3] =='AluYb9':
            AluYb9.append(list)
        elif list[3]=='AluYc':
            AluYc.append(list)
        elif list[3] =='AluYc3':
            AluYc3.append(list)
        elif list[3]=='AluYc5':
            AluYc5.append(list)
        elif list[3] =='AluYd8':
            AluYd8.append(list)
        elif list[3]=='AluYg6':
            AluYg6.append(list)
        elif list[3] =='AluYh9':
            AluYh9.append(list)
    
#    for repeat in AluSp[-500:-1]:
#        print repeat
        
    AluRepeats = [AluSp, AluSx, AluSc, AluSq, AluSg, AluSg1, AluJo, AluJ, AluJb, AluY, AluYa5, AluYa8, AluYb8, AluYb9, AluYc, AluYc3, AluYc5, AluYd8, AluYg6, AluYh9]
    
    if param == 'all':
        return AluRepeats
    elif param == 'AluSp':
        return AluSp
    elif param == 'AluSx':
        return AluSx
    elif param == 'AluSc':
        return AluSc
    elif param == 'AluSq':
        return AluSq
    elif param == 'AluSg':
        return AluSg
    elif param == 'AluSg1':
        return AluSg1
    elif param == 'AluJo':
        return AluJo
    elif param == 'AluJ':
        return AluJ
    elif param == 'AluJb':
        return AluJb
    elif param == 'AluY':
        return AluY
    elif param == 'AluYa5':
        return AluYa5
    elif param == 'AluYa8':
        return AluYa8
    elif param == 'AluYb8':
        return AluYb8
    elif param == 'AluYb9':
        return AluYb9
    elif param == 'AluYc':
        return AluYc
    elif param == 'AluYc3':
        return AluYc3
    elif param == 'AluYc5':
        return AluYc5
    elif param == 'AluYd8':
        return AluYd8
    elif param == 'AluYg6':
        return AluYg6
    elif param == 'AluYh9':
        return AluYh9
  

"""
Find takes in one line of string as a parameter and splits the words delimited by whitespace and makes a list of the words.
@param : str : one line of string 
@return: a list of words contained in the str, separated by whitespace 
"""
def Find(str):
    plist = str.split()
    list = [plist[0], int(plist[1]), int(plist[2]), plist[3], int(plist[4]), plist[5] ]
    return list


"""
@param list: takes in a list of lists
@return: doesnt return anything, just prints each list of the whole big list in a new line.
"""
def Print(list):
    for line in list:
        print line


def main():
    file = sys.argv[1]
    Print(AluRep(file, 'AluY'))   
 

"""
default boilerplate
"""

if __name__ == '__main__':
    main()
