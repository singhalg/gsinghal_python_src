'''
Created on Dec 28, 2011

@author: Gaurav Singhal
'''
import sys


from Bio import Entrez, Medline
Entrez.email = "gaurav.singhal.01@gmail.com"

"""
Usage :
python getAbstracts numResults  filename keywords

Example:

python getAbstracts.py 50 abs1.txt lung cancer

@arg : numResults : The number of search results to be retrieved
@arg : filename : The results will be saved in filename.txt. The filename must be a single word.
@arg : keywords : eg, lung cancer

@return: Saves a text file with the filename having the Medline information from PubMed entries in the following format.

Title :  The EGFR T790M mutation in acquired resistance to an irreversible second-generation EGFR inhibitor.

Journal/Date :  Mol Cancer Ther. 2012 Jan 6.      Pubmed Id:  22228822

Abstract :  Molecular target therapi

"""

def getpmedAbstracts(numResults,  filename, keywords):

    handle = Entrez.esearch(db="pubmed", term=keywords, retmax=numResults )

    # http://www.ncbi.nlm.nih.gov/entrez/query/static/esearch_help.html

    #handle = Entrez.egquery("lung cancer") # E-Global Query

    record = Entrez.read(handle)

    idlist = record["IdList"]

    allAbs = Entrez.efetch(db="pubmed", id = idlist, rettype="medline", retmode="text")
    abstracts = Medline.parse(allAbs)

    absList = []

    filename+='.txt'
#    print idlist
#    print record
#    print '\n'
    output =  open(filename, 'w')
    ab = list(abstracts)
    for each in ab:

        ti =  "Title : " + each.get("TI", "?") + '\n'
        output.write(ti)

        jd = "Journal/Date : " + each.get("SO", "?") +'\t' + " Pubmed Id: " + each.get("PMID", "?") + '\n'
        output.write(jd)

        abs = "Abstract : " + each.get("AB", "?")+ '\n\n\n'
        output.write(abs)
        absList.append(each.get("AB", "?"))

#        output.write(str(fl)+str(sl)+str(tl))


    output.close()
    return absList

# 23      AB        Abstract
# 24      CI        Copyright Information
# 25      AD        Affiliation
# 26      IRAD      Investigator Affiliation
# 27      AID       Article Identifier
# 28      AU        Author
# 29      FAU       Full Author
# 30      CN        Corporate Author
# 31      DCOM      Date Completed
# 32      DA        Date Created
# 33      LR        Date Last Revised
# 34      DEP       Date of Electronic Publication
# 35      DP        Date of Publication
# 36      EDAT      Entrez Date
# 37      GS        Gene Symbol
# 38      GN        General Note
# 39      GR        Grant Number
# 40      IR        Investigator Name
# 41      FIR       Full Investigator Name
# 42      IS        ISSN
# 43      IP        Issue
# 44      TA        Journal Title Abbreviation
# 45      JT        Journal Title
# 46      LA        Language
# 47      LID       Location Identifier
# 48      MID       Manuscript Identifier
# 49      MHDA      MeSH Date
# 50      MH        MeSH Terms
# 51      JID       NLM Unique ID
# 52      RF        Number of References
# 53      OAB       Other Abstract
# 54      OCI       Other Copyright Information
# 55      OID       Other ID
# 56      OT        Other Term
# 57      OTO       Other Term Owner
# 58      OWN       Owner
# 59      PG        Pagination
# 60      PS        Personal Name as Subject
# 61      FPS       Full Personal Name as Subject
# 62      PL        Place of Publication
# 63      PHST      Publication History Status
# 64      PST       Publication Status
# 65      PT        Publication Type
# 66      PUBM      Publishing Model
# 67      PMC       PubMed Central Identifier
# 68      PMID      PubMed Unique Identifier
# 69      RN        Registry Number/EC Number
# 70      NM        Substance Name
# 71      SI        Secondary Source ID
# 72      SO        Source
# 73      SFM       Space Flight Mission
# 74      STAT      Status
# 75      SB        Subset
# 76      TI        Title
# 77      TT        Transliterated Title
# 78      VI        Volume
# 79      CON       Comment on
# 80      CIN       Comment in
# 81      EIN       Erratum in
# 82      EFR       Erratum for
# 83      CRI       Corrected and Republished in
# 84      CRF       Corrected and Republished from
# 85      PRIN      Partial retraction in
# 86      PROF      Partial retraction of
# 87      RPI       Republished in
# 88      RPF       Republished from
# 89      RIN       Retraction in
# 90      ROF       Retraction of
# 91      UIN       Update in
# 92      UOF       Update of
# 93      SPIN      Summary for patients in
# 94      ORI       Original report in


def processData(num, filename, query):
    absList = getpmedAbstracts(num,  filename, query)



    return absList





def main ():

    numResults = sys.argv[1]
    num = int(numResults)
    filename = sys.argv[2]
    keywords = sys.argv[3:]
    query = ''
    for each in keywords:
        query= query+each+' '




    getpmedAbstracts(num, filename, query)
    processData(num, filename, query)


if __name__=='__main__':
    main()

