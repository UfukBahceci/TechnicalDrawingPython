import numpy as np
class Vertex:
    def __init__(self,positionwrobjvect,obj):
        self.positionwrobj = positionwrobjvect
        self.obj=obj
    def refresh(self):
        self.positionwrcam=np.array([[0.,0.,0.,1.]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.positionwrcam=np.row_stack([self.positionwrcam,[0.,0.,0.,1.]])
        self.positionperstfwrcam=np.array([[0.,0.,0.,1.]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.positionperstfwrcam=np.row_stack([self.positionperstfwrcam,[0.,0.,0.,1.]])
        self.positionprjztfwrcam=np.array([[0.,0.,0.,1.]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.positionprjztfwrcam=np.row_stack([self.positionprjztfwrcam,[0.,0.,0.,1.]])
    def setpositionwrcam(self,positionwrcamvect,index):
        self.positionwrcam[index] = positionwrcamvect
    def getpositionwrcam(self,index):
        return self.positionwrcam[index]
    def setpositionperstfwrcam(self,positionperstfwrcamvect,index):
        self.positionperstfwrcam[index] = positionperstfwrcamvect
    def getpositionperstfwrcam(self,index):
        return self.positionperstfwrcam[index]
    def setpositionprjztfwrcam(self,positionprjztfwrcamvect,index):
        self.positionprjztfwrcam[index] = positionprjztfwrcamvect
    def getpositionprjztfwrcam(self,index):
        return self.positionprjztfwrcam[index]