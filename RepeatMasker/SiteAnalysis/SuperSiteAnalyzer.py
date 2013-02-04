'''
Created on Jun 14, 2010

@author: Gaurav
'''


from SiteAnalyzer1 import siteAnalyzer
from SiteAnalyzer1 import manyplots
from SiteAnalyzer1 import printScore
import sys


'''
This method is the key method that is run with the required arguments to produce a plot pf per base consensus scores.
This method makes calls to other methods and supplied them the required arguments. 
It creates a plot of per base consensus scores for a repeat element for three different restriction sites.
'''
def SuperSiteAnalyzer(repeat, site1, site2,  site3, site1name, site2name, site3name, save):
    consensus1 = siteAnalyzer(repeat, site1)
    consensus2 = siteAnalyzer(repeat, site2)
    consensus3 = siteAnalyzer(repeat, site3)
    
    #printing scores to output files named as repeat_site1name_score
    printScore(consensus1, site1name, repeat)
    printScore(consensus2, site2name, repeat)
    printScore(consensus3, site3name, repeat)
    
    #plot is made and saved to file named as repeat_RS.png
    manyplots(repeat, consensus1, site1name, consensus2, site2name, consensus3, site3name, save)
    




def main():
    repeat = sys.argv[1]
    site1 = sys.argv[2]
    site1name = sys.argv[3]
    site2 = sys.argv[4]
    site2name = sys.argv[5]
    site3 = sys.argv[6]
    site3name = sys.argv[7]
    save = sys.argv[8]
    SuperSiteAnalyzer(repeat, site1, site2,  site3, site1name, site2name, site3name, save)
    
    
if __name__ =='__main__':
    main()