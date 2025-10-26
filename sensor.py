import numpy as np

import pyrosim.pyrosim as pyrosim


class SENSOR:

    def __init__(self, linkName, steps):
        self.linkName = linkName
        self.steps = steps
        self.values = np.zeros(steps)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save('data/' + self.linkName + 'SensorValues.npy', self.values)
