import pybullet as p

physicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()

p.disconnect()
