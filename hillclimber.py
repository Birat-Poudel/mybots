import copy

import constants as c
from solution import SOLUTION


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currGeneration in range(c.NUM_GENERATIONS):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")
        
        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child
    
    def Print(self):
        print("Parent Fitness: ", self.parent.fitness, "Child Fitness: ", self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        print("Best:", self.parent.fitness)
