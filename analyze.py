import numpy as np
import matplotlib.pyplot as plt
backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
BtargetAngles = np.load("data/BtargetAngles.npy")
FtargetAngles = np.load("data/FtargetAngles.npy")

plt.plot(BtargetAngles,label = "BtargetAngles")
plt.plot(FtargetAngles,label = "FtargetAngles")

#plt.plot(backLegSensorValues,label = "backLegSensorValues")
#plt.plot(frontLegSensorValues,label = "frontLegSensorValues")
plt.legend()
plt.show()
