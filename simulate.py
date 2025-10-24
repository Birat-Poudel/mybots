import time
import pybullet as p

physicsClient = p.connect(p.GUI)

for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/120)

p.disconnect()
