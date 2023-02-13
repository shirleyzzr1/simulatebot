import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
for i in range(100):
    p.stepSimulation()
    print("i: ",i)
    time.sleep(1.0/60)
p.disconnect()
