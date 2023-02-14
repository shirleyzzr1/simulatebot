import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
x = np.linspace(0,2*np.pi,1000)
#targetAngles = np.sin(x)*np.pi/4
Bamplitude,Bfrequency,BphaseOffset = np.pi/4,10,0
BtargetAngles = [Bamplitude*np.sin(Bfrequency*x[i]+BphaseOffset) for i in range(len(x))]
Famplitude,Ffrequency,FphaseOffset = np.pi/4,10,0
FtargetAngles = [Famplitude*np.sin(Ffrequency*x[i]+FphaseOffset) for i in range(len(x))]

#np.save("./data/BtargetAngles",BtargetAngles)
#np.save("./data/FtargetAngles",FtargetAngles)
#exit()
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = FtargetAngles[i],
        maxForce = 20)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = BtargetAngles[i],
        maxForce = 20)
    time.sleep(1.0/60)
#print("backLegSensorValues: ",backLegSensorValues)
np.save("./data/backLegSensorValues",backLegSensorValues)
np.save("./data/frontLegSensorValues",frontLegSensorValues)

p.disconnect()
