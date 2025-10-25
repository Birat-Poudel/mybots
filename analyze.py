import os

import numpy as np
import matplotlib.pyplot as plt


base_dir = os.path.dirname(__file__)
backLegSensorValuesPath = os.path.join(base_dir, "data", "back_leg_sensor_values.npy")
frontLegSensorValuesPath = os.path.join(base_dir, "data", "front_leg_sensor_values.npy")

backLegSensorValues = None
frontLegSensorValues = None

if os.path.exists(backLegSensorValuesPath):
    backLegSensorValues = np.load(backLegSensorValuesPath)
if os.path.exists(frontLegSensorValuesPath):
    frontLegSensorValues = np.load(frontLegSensorValuesPath)

if backLegSensorValues is None and frontLegSensorValues is None:
    raise FileNotFoundError("Could not find sensor values!")

plt.figure()

if backLegSensorValues is not None:
    plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)

if frontLegSensorValues is not None:
    plt.plot(frontLegSensorValues, label="Front Leg")

plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0.)

output_path = os.path.join(base_dir, "data", "sensor_trajectories.png")
plt.savefig(output_path, dpi=200, bbox_inches="tight")
