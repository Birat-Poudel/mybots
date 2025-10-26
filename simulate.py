import sys

import constants as c
from simulation import SIMULATION


directOrGui = sys.argv[1]

simulation = SIMULATION(c.STEPS, directOrGui)
simulation.Run()
simulation.Get_Fitness()
