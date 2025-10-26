import time

import constants as c
import pybullet as p
import pybullet_data

from robot import ROBOT
from world import WORLD


class SIMULATION:

    def __init__(self, steps):
        self.physicsClient = p.connect(p.GUI)
        self.steps = steps

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-c.GRAVITY,self.physicsClient)

        self.world = WORLD()
        self.robot = ROBOT(self.steps)

    def Run(self):
        for t in range(self.steps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            time.sleep(c.SLEEP)

    def __del__(self):
        p.disconnect()
