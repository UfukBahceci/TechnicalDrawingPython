import numpy as np
class Surface:
    def __init__(self,obj):
        self.edgeloop=[]
        self.orderedvertexlist=[]
        self.obj=obj
    def refresh(self):
        self.normal=np.array([[0.,0.,0.,1.]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.normal=np.row_stack([self.normal,[0.,0.,0.,1.]])
        self.unrealisticshadingintensity=np.array([[0.]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.unrealisticshadingintensity=np.row_stack([self.unrealisticshadingintensity,[0.]])
        self.planeXwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeXwrcam=np.row_stack([self.planeXwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeYwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeYwrcam=np.row_stack([self.planeYwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeZwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeZwrcam=np.row_stack([self.planeZwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])        
        self.planeXperstfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeXperstfwrcam=np.row_stack([self.planeXperstfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeYperstfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeYperstfwrcam=np.row_stack([self.planeYperstfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeZperstfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeZperstfwrcam=np.row_stack([self.planeZperstfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])        
        self.planeXprjztfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeXprjztfwrcam=np.row_stack([self.planeXprjztfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeYprjztfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeYprjztfwrcam=np.row_stack([self.planeYprjztfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])
        self.planeZprjztfwrcam=np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])
        for index in range(len(self.obj.scene.cameralist)-1):         
            self.planeZprjztfwrcam=np.row_stack([self.planeZprjztfwrcam,np.array([[np.zeros(len(self.orderedvertexlist)),np.zeros(len(self.orderedvertexlist))]])])    
    def setnormal(self,normalvect,index):
        self.normal[index] = normalvect
    def getnormal(self,index):
        return self.normal[index]
    def setunrealisticshadingintensity(self,unrealisticshadingintensityvect,index):
        self.unrealisticshadingintensity[index] = unrealisticshadingintensityvect
    def getunrealisticshadingintensity(self,index):
        return self.unrealisticshadingintensity[index]
    def setplaneXwrcam(self,matrix,index):
        self.planeXwrcam[index] = matrix
    def getplaneXwrcam(self,index):
        return self.planeXwrcam[index]
    def setplaneYwrcam(self,matrix,index):
        self.planeYwrcam[index] = matrix
    def getplaneYwrcam(self,index):
        return self.planeYwrcam[index]
    def setplaneZwrcam(self,matrix,index):
        self.planeZwrcam[index] = matrix
    def getplaneZwrcam(self,index):
        return self.planeZwrcam[index]
    def setplaneXperstfwrcam(self,matrix,index):
        self.planeXperstfwrcam[index] = matrix
    def getplaneXperstfwrcam(self,index):
        return self.planeXperstfwrcam[index]
    def setplaneYperstfwrcam(self,matrix,index):
        self.planeYperstfwrcam[index] = matrix
    def getplaneYperstfwrcam(self,index):
        return self.planeYperstfwrcam[index]
    def setplaneZperstfwrcam(self,matrix,index):
        self.planeZperstfwrcam[index] = matrix
    def getplaneZperstfwrcam(self,index):
        return self.planeZperstfwrcam[index]
    def setplaneXprjztfwrcam(self,matrix,index):
        self.planeXprjztfwrcam[index] = matrix
    def getplaneXprjztfwrcam(self,index):
        return self.planeXprjztfwrcam[index]
    def setplaneYprjztfwrcam(self,matrix,index):
        self.planeYprjztfwrcam[index] = matrix
    def getplaneYprjztfwrcam(self,index):
        return self.planeYprjztfwrcam[index]
    def setplaneZprjztfwrcam(self,matrix,index):
        self.planeZprjztfwrcam[index] = matrix
    def getplaneZprjztfwrcam(self,index):
        return self.planeZprjztfwrcam[index]
    def add_edge(self,edgeobj):
        self.edgeloop.append(edgeobj)
    def find_orderedvertexlist(self):
        self.orderedvertexlist.append(self.edgeloop[0].fromvertex)
        lastaddedvertex=self.edgeloop[0].fromvertex
        for index in range(len(self.edgeloop)-1):
            tobeaddedvertex=self.edgeloop[index+1].tovertex
            if tobeaddedvertex == lastaddedvertex:
                tobeaddedvertex=self.edgeloop[index+1].fromvertex
            elif self.edgeloop[index+1].fromvertex == lastaddedvertex:
                pass
            elif ((self.edgeloop[index+1].fromvertex == self.edgeloop[index].fromvertex)or(self.edgeloop[index+1].fromvertex == self.edgeloop[index].tovertex)):
                tobeaddedvertex=self.edgeloop[index+1].fromvertex
            else:
                tobeaddedvertex=self.edgeloop[index+1].tovertex
            self.orderedvertexlist.append(tobeaddedvertex)
            lastaddedvertex=tobeaddedvertex
    def calculate_normal(self,linearobj,index):
        vector1=self.orderedvertexlist[0].getpositionwrcam(index)
        vector2=self.orderedvertexlist[1].getpositionwrcam(index)
        vector3=self.orderedvertexlist[2].getpositionwrcam(index)
        self.setnormal(linearobj.transformations.calculate_planenormalfromthreepoints(vector1,vector2,vector3),index)
        dvectorfromorijintosurfacepoint=linearobj.transformations.calculate_directionfrompoint1topoint2(linearobj.orijin.getpositionwrcam(index),vector1)
        if linearobj.transformations.dot_vectors(dvectorfromorijintosurfacepoint,self.getnormal(index)) < 0:
            self.setnormal(linearobj.transformations.reverse_direction(self.getnormal(index)),index)
    def calculate_unrealisticshadingintensity(self,linearobj,index):
        camtosurfacedvector=np.array([0.,0.,0.,0.])
        for v in self.orderedvertexlist:
            camtosurfacedvector=camtosurfacedvector+v.getpositionwrcam(index)       
        camtosurfacedvector=linearobj.transformations.homogenproject_vector(camtosurfacedvector)
        unrealisticshadingintensity=linearobj.transformations.dot_vectors(camtosurfacedvector,self.getnormal(index))
        if unrealisticshadingintensity > 0:
            unrealisticshadingintensity = 0
        elif unrealisticshadingintensity < -1:
            unrealisticshadingintensity = -1
        unrealisticshadingintensity = -unrealisticshadingintensity
        self.setunrealisticshadingintensity(np.array([unrealisticshadingintensity]),index)
    def generate_planecoordinateswrcam(self,index):
        vertexXlistfirstrow=[]
        vertexYlistfirstrow=[]
        vertexZlistfirstrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistfirstrow.append(self.orderedvertexlist[vindex].getpositionwrcam(index)[0])
            vertexYlistfirstrow.append(self.orderedvertexlist[vindex].getpositionwrcam(index)[1])
            vertexZlistfirstrow.append(self.orderedvertexlist[vindex].getpositionwrcam(index)[2])
        vertexXlistsecondrow=[]
        vertexYlistsecondrow=[]
        vertexZlistsecondrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistsecondrow.append(self.orderedvertexlist[0].getpositionwrcam(index)[0])
            vertexYlistsecondrow.append(self.orderedvertexlist[0].getpositionwrcam(index)[1])
            vertexZlistsecondrow.append(self.orderedvertexlist[0].getpositionwrcam(index)[2])       
        self.setplaneXwrcam(np.array([vertexXlistfirstrow,vertexXlistsecondrow]),index)
        self.setplaneYwrcam(np.array([vertexYlistfirstrow,vertexYlistsecondrow]),index)
        self.setplaneZwrcam(np.array([vertexZlistfirstrow,vertexZlistsecondrow]),index)
    def generate_planecoordinatesperstfwrcam(self,index):
        vertexXlistfirstrow=[]
        vertexYlistfirstrow=[]
        vertexZlistfirstrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistfirstrow.append(self.orderedvertexlist[vindex].getpositionperstfwrcam(index)[0])
            vertexYlistfirstrow.append(self.orderedvertexlist[vindex].getpositionperstfwrcam(index)[1])
            vertexZlistfirstrow.append(self.orderedvertexlist[vindex].getpositionperstfwrcam(index)[2])
        vertexXlistsecondrow=[]
        vertexYlistsecondrow=[]
        vertexZlistsecondrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistsecondrow.append(self.orderedvertexlist[0].getpositionperstfwrcam(index)[0])
            vertexYlistsecondrow.append(self.orderedvertexlist[0].getpositionperstfwrcam(index)[1])
            vertexZlistsecondrow.append(self.orderedvertexlist[0].getpositionperstfwrcam(index)[2])       
        self.setplaneXperstfwrcam(np.array([vertexXlistfirstrow,vertexXlistsecondrow]),index)
        self.setplaneYperstfwrcam(np.array([vertexYlistfirstrow,vertexYlistsecondrow]),index)
        self.setplaneZperstfwrcam(np.array([vertexZlistfirstrow,vertexZlistsecondrow]),index)
    def generate_planecoordinatesprjztfwrcam(self,index):
        vertexXlistfirstrow=[]
        vertexYlistfirstrow=[]
        vertexZlistfirstrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistfirstrow.append(self.orderedvertexlist[vindex].getpositionprjztfwrcam(index)[0])
            vertexYlistfirstrow.append(self.orderedvertexlist[vindex].getpositionprjztfwrcam(index)[1])
            vertexZlistfirstrow.append(self.orderedvertexlist[vindex].getpositionprjztfwrcam(index)[2])
        vertexXlistsecondrow=[]
        vertexYlistsecondrow=[]
        vertexZlistsecondrow=[]
        for vindex in range(len(self.orderedvertexlist)):
            vertexXlistsecondrow.append(self.orderedvertexlist[0].getpositionprjztfwrcam(index)[0])
            vertexYlistsecondrow.append(self.orderedvertexlist[0].getpositionprjztfwrcam(index)[1])
            vertexZlistsecondrow.append(self.orderedvertexlist[0].getpositionprjztfwrcam(index)[2])       
        self.setplaneXprjztfwrcam(np.array([vertexXlistfirstrow,vertexXlistsecondrow]),index)
        self.setplaneYprjztfwrcam(np.array([vertexYlistfirstrow,vertexYlistsecondrow]),index)
        self.setplaneZprjztfwrcam(np.array([vertexZlistfirstrow,vertexZlistsecondrow]),index)