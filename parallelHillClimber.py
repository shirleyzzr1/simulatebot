from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self) -> None:
        self.nextAvailableID = 0

        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
    
    def Evolve(self):
        # for idx in self.parents:
        #     # self.parents[idx].Evaluate("GUI")
        #     self.parents[idx].Start_Simulation("DIRECT")
        # for idx in self.parents:
        #     # self.parents[idx].Evaluate("GUI")
        #     self.parents[idx].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        self.children = {}
        for idx in self.parents:
            self.children[idx] = copy.deepcopy(self.parents[idx])
            self.children[idx].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1

    def Mutate(self):
        for idx in self.children:
            self.children[idx].Mutate()

    def Select(self):
        #parent is worse than child's fitness
        for idx in self.children:      
            if self.parents[idx].fitness>self.children[idx].fitness:
                print("choose child fitness")
                self.parents[idx] = copy.deepcopy(self.children[idx])
            # self.parent = self.child

    def Print(self):
        print("\n")
        for idx in self.children:
            print("parent fitness: {}, child fitness: {}".format(self.parents[idx].fitness,self.children[idx].fitness))

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        bestparent = SOLUTION(-1)
        bestfitness = 1000
        for idx in self.parents:
            if self.parents[idx].fitness<bestfitness:
                bestparent = copy.deepcopy(self.parents[idx])
        bestparent.Start_Simulation("GUI")
        

    def Evaluate(self,solutions):
        for idx in self.parents:
            # self.parents[idx].Evaluate("GUI")
            solutions[idx].Start_Simulation("DIRECT")
        for idx in self.parents:
            solutions[idx].Wait_For_Simulation_To_End()


