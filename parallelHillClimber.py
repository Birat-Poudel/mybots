import os
import copy

import constants as c
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm fitness*.txt")
        os.system("rm brain*.nndf")

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currGeneration in range(c.NUM_GENERATIONS):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)
        print("\n")
        self.Print()
        print("\n")

        self.Select()


    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()


    def Select(self):
        for keyp, keyc in zip(self.parents.keys(), self.children.keys()):
            if self.children[keyc].fitness < self.parents[keyp].fitness:
                self.parents[keyp] = copy.deepcopy(self.children[keyc])


    def Print(self):
        for keyp, keyc in zip(self.parents.keys(), self.children.keys()):
            print("Parent:", self.parents[keyp].fitness, "Child:", self.children[keyc].fitness)


    def Show_Best(self):
        bestKey = 0
        bestFitness = float('inf')
        for key in self.parents.keys():
            if self.parents[key].fitness < bestFitness:
                bestKey = key
                bestFitness = self.parents[key].fitness

        bestSolution = copy.deepcopy(self.parents[bestKey])  
        bestSolution.Start_Simulation("GUI")  

    
    def Evaluate(self, solutions):
        for individual in solutions:
            solutions[individual].Start_Simulation("DIRECT")
        
        for individual in solutions:
            solutions[individual].Wait_For_Simulation_To_End()
