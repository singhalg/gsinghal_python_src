'''
Created on Mar 16, 2012

@author: gsinghal
'''
import sys

def bayes(filename):
    
    
    fh = open(filename, 'rU')
    fields = fh.readline()
    txt = fh.readlines()
    fh.close()
    
    data = []
    
    for line in txt:   
        data.append(line.split(','))
        
    
    binClass = []
    bin = [0,1]
    for one in bin:
        for two in bin:
            for three in bin:
                for four in bin:
                    atup = (one, two, three, four)
                    binClass.append(atup)
#    
    
     
    
    Temperature = ['Hot', 'Cold']
    Humidity = ['Humid', 'Dry']
    Brightness = ['Bright', 'Dim']
    Cloud = ['Cloudy', 'Sunny']
    
    classes = []
    
    for one in Temperature:
        for two in Humidity:
            for three in Brightness:
                for four in Cloud:
                    classes.append([one, two, three, four]) 
    
    
    print '# classes' , len(classes)
    print '# binClass' , len(binClass)

    
#    for i in range(16):
#        print binClass[i], classes[i]
        
    p = [0]*16
    
    for eachRow in data:
        for eachClass in classes:
            if eachClass == eachRow[:4]:
                i = classes.index(eachClass)
                p[i]+=1
                break
    
    
    
    print p
    
    total = len(p)
    print total
    
    prob = []
    for eachnum in p:
        prob.append(float(eachnum))

    prob = [(item/total) for item in prob]
    
    for i in range(16):
        print binClass[i], classes[i], prob[i]


    print '#############################################################################################'
    
    
#    #####################+++++++++++++++++++++++++++++====================___________________________+++++++++++++++++++++##################


    binClassS = []
    for one in bin:
        for two in bin:
            for three in bin:
                atup = (one, two, three)
                binClassS.append(atup)
#    

    
    classesS = []
    
    for one in Temperature:
        for two in Brightness:
            for three in Cloud:
                classesS.append([one, two, three]) 
    
    
    print '# classes in short-classes' , len(classesS)
    print '# binClass in binClasses' , len(binClassS)

    
#    for i in range(16):
#        print binClass[i], classes[i]
        
    ps  = [0]*8
    
    for eachRow in data:
        for eachClass in classesS:
            if eachClass == [eachRow[0], eachRow[2], eachRow[3]]:
                i = classesS.index(eachClass)
                ps[i]+=1
                break
    
    
    
    print ps
    
    total = len(ps)
    print total
    
    probS = []
    for eachnum in ps:
        probS.append(float(eachnum))

    probS = [(item/total) for item in probS]
    
    for i in range(8):
        print binClassS[i], classesS[i], probS[i]

    
    
    
    
    
    print probS
#    print data[5][:4]
    print fields, data
    
    print '=========================================================='
    
    
    yn  = [0]*2
    
    for eachRow in data:
        
        if eachRow[4].strip()== 'y':
            yn[0]+=1
        else:
            yn[1]+=1
            
        
    numInst = float(sum(yn))
    yes = float(yn[0])/numInst
    no = float(yn[1])/numInst
    
    print yn
    print 'yes = ', yes, ';  no = ', no
    
    print '=============================================================='
    
    
    pCold_Y = 0
    pDim_Y = 0
    pSunny_Y = 0
    
    pCold_N = 0
    pDim_N = 0
    pSunny_N = 0
    
    pBright_Y = 0
    pBright_N = 0
    
    pDry_Y = 0
    pDry_N = 0
    
    
    
    for eachRow in data:
        
        if eachRow[4].strip()== 'y':
            if eachRow[0]=='Cold':
                pCold_Y+=1
            if eachRow[2] == 'Dim':
                pDim_Y+=1
            if eachRow[2] =='Bright':
                pBright_Y+=1
            if eachRow[3] == 'Sunny':
                pSunny_Y+=1
            if eachRow[1]=='Dry':
                pDry_Y+=1
        else:
            if eachRow[0]=='Cold':
                pCold_N+=1
            if eachRow[2] == 'Dim':
                pDim_N+=1
            if eachRow[2] =='Bright':
                pBright_N+=1
            if eachRow[3] == 'Sunny':
                pSunny_N+=1
            if eachRow[1]=='Dry':
                pDry_N+=1

    
    
    print pCold_Y, pDim_Y, pSunny_Y, pCold_N,pDim_N , pSunny_N, pBright_Y, pBright_N, pDry_Y, pDry_N
    
    print 'Cold|Y = ', pCold_Y        
    print 'Cold|N = ', pCold_N
    
    print 'Dim|Y = ', pDim_Y
    print 'Dim|N = ', pDim_N
    
    print 'Sunny|Y = ', pSunny_Y 
    print 'Sunny|N = ', pSunny_N
    
    print 'Bright|Y = ', pBright_Y
    print 'Bright|N = ', pBright_N
    
    print 'Dry|Y = ', pDry_Y
    print 'Dry|N = ', pDry_N
    
    
    # adding pseudocount for pDim_Y
    yn[0]+=1
    
    pDim_Y+=1
    
    print 'after adding pseudocount'
    print pCold_Y, pDim_Y, pSunny_Y, pCold_N,pDim_N , pSunny_N, pBright_Y, pBright_N, pDry_Y, pDry_N
    
    pCold_Y = float(pCold_Y)/yn[0]
    
    pDim_Y = float(pDim_Y)/yn[0]
    
    pBright_Y = float(pBright_Y)/yn[0]
    
    pSunny_Y = float(pSunny_Y)/yn[0]
    
    pDry_Y = float(pSunny_Y)/yn[0]
    
    
    pCold_N = float(pCold_N)/yn[1]
    
    pDim_N = float(pDim_N)/yn[1]
    
    pBright_N = float(pBright_N)/yn[1]
    
    pSunny_N = float(pSunny_N)/yn[1]
    
    pDry_N = float(pDry_N)/yn[1]
    
    
#    1 0 1 18 13 10 14 9
#0.0714285714286 0.0 0.0714285714286 0.818181818182 0.590909090909 0.454545454545 1.0 0.409090909091
  
    
    print pCold_Y, pDim_Y,  pSunny_Y, pCold_N,pDim_N , pSunny_N, pBright_Y, pBright_N, pDry_Y, pDry_N
    
    print 'pCold|Y = ', pCold_Y        
    print 'pCold|N = ', pCold_N
    
    print 'pDim|Y = ', pDim_Y
    print 'pDim|N = ', pDim_N
    
    print 'pSunny|Y = ', pSunny_Y 
    print 'pSunny|N = ', pSunny_N
    
    print 'pBright|Y = ', pBright_Y
    print 'pBright|N = ', pBright_N
    
    print 'pDry|Y = ', pDry_Y
    print 'pDry|N = ', pDry_N
    
def main():
    fileName = sys.argv[1]
    bayes(fileName)

if __name__=='__main__':
    main()