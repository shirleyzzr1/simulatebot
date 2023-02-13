import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
for i in range(1000):
    p.stepSimulation()
    print("i: ",i)
    time.sleep(1.0/60)
p.disconnect()
