'''
Created on Oct 6, 2010

@author: Gaurav Singhal
'''

import simuPOP a

import simuPOP as sim

pop = sim.Population(size=1000, loci=[2])
pop.evolve(initOps = [sim.InitSex(),sim.initGenotype(pop, genotype=[1, 2, 2, 1])],  matingScheme=sim.RandomMating(ops=sim.Recombinator(rates=0.01)),
    postOps = [sim.stat(pop, LD=[0, 1]),sim.PyEval(r"'%.2f\n' % LD[0][1]", step=10),],gen=100)


