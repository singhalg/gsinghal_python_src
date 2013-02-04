'''
Created on Sep 2, 2010

@author: Gaurav
'''





import simuPOP as sim




#help(sim.Population.addInfoFields)

pop = sim.Population(size = 100, loci=2, ploidy =2, alleleNames=['A', 'T'], ancGen = -1, infoFields = ['selectCoeff', 'Dominance'])
# size = population size, loci = no of chromosomes, ploidy = diploid / haploid, allele

pop.evolve(initOps = 
           [sim.InitSex(), 
            sim.InitGenotype(genotype = [1,2,2,1,])], 
           matingScheme = sim.RandomMating(ops = sim.Recombinator(rates=0.1)),
           gen=100)

print 'ploidy = ', +  pop.ploidy()

print pop.ploidyName()


print pop.alleleName(1)
