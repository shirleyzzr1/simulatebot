import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length,width,height = 1,1,1
x,y,z = 0,0,0.5
for i in range(10):
    pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
    z+=(height/2)
    length*=0.9
    width*=0.9
    height*=0.9
    z+=(height/2)

#pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
#pyrosim.Send_Cube(name="Box2",pos=[x2,y2,z2],size=[length,width,height])
pyrosim.End()

