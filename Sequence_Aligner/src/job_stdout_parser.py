#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     19/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os


def job_output_parser(filename):
    outfile = open('smp_report.csv', 'w')
    outfile.write('Processes, CPU-Time, Wall-Time, Memory, Virtual Memory \n')
    i = 1
    for each in filename:


        fh = open(each, 'rU')

        data  = fh.readlines()
        fh.close()
        resource = data[16]
        print resource
        cputS = resource.rfind('cput')
        cputE = resource.find(',mem')
        time =  resource[cputS+5:cputE]
        hms = time.split(':')
        CPUmins = (int(hms[0])*60) + (int(hms[1])) + (float(hms[2])/60)



        wallS = resource.rfind('walltime')

        time =  resource[wallS+9:]
        hms = time.split(':')
        wallmins = (int(hms[0])*60) + (int(hms[1])) + (float(hms[2])/60)

        memS = resource.rfind(',mem=')
        memE = resource.find('kb,vmem')
        mem =  resource[memS+5:memE]
        mem = (float(mem)/1048576)

        vmemS = resource.rfind('vmem=')
        vmemE = resource.find('kb,wall')
        vmem =  resource[vmemS+5:vmemE]
        vmem = (float(vmem)/1048576)

        procs = str(i*8)
        outline =  procs+','+ str(CPUmins)+ ','+ str(wallmins)+ ','+ str(mem)+ ','+ str(vmem) + '\n'
        outfile.write(outline)
        i+=1

    outfile.close()





def main():

    files = []
    files.append('gsinghal_NA18519_hg19_paired_8.o1588108')
    files.append('gsinghal_NA18519_hg19_paired_16.o1588112')
    files.append('gsinghal_NA18519_hg19_paired_24.o1588113')
    files.append('gsinghal_NA18519_hg19_paired_32.o1588109')
    files.append('gsinghal_NA18519_hg19_paired_40.o1588110')
    files.append('gsinghal_NA18519_hg19_paired_48.o1588114')
    files.append('gsinghal_NA18519_hg19_paired_56.o1588115')
    files.append('gsinghal_NA18519_hg19_paired_64.o1588111')




    job_output_parser(files)

if __name__ == '__main__':
    main()
