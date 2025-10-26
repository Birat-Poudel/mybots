import sys

import constants as c
from simulation import SIMULATION


directOrGui = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(c.STEPS, directOrGui, solutionID)
simulation.Run()
simulation.Get_Fitness()
