import numpy as np
class Camera:
    def __init__(self,azim,dist,elev,sceneobj,name,viewlimits):
        self.reset_position()
        self.copfocalsxyzinfinity = -1000000
        self.name = name
        self.viewlimits = viewlimits # None or [minoflimits,maxoflimits]
        self.scene = sceneobj
        self.scene.currentcamindex = self.scene.currentcamindex + 1
        self.ax = self.scene.fig.add_subplot(self.scene.numberofcams+1,1,self.scene.currentcamindex,projection='3d')
        self.ax.azim = azim
        self.ax.dist = dist
        self.ax.elev = elev
        self.transformations = self.scene.tf
        self.cameratfgen = False
        self.persorobliquetfgen = False
        self.prjztfgen = True
        self.traceptgen = False
        self.vrfraypersgen = False
        self.vrfrayobliquegen = False
    def set_generateviewbools(self,cameratfgen,persorobliquetfgen,prjztfgen,traceptgen,vrfraypersgen,vrfrayobliquegen):
        self.cameratfgen = cameratfgen
        self.persorobliquetfgen = persorobliquetfgen
        self.prjztfgen = prjztfgen
        self.traceptgen = traceptgen
        self.vrfraypersgen = vrfraypersgen
        self.vrfrayobliquegen = vrfrayobliquegen
    def clear(self):
        self.ax.clear()
        self.ax.set_xlabel('x')
        self.ax.xaxis.label.set_color('red')
        self.ax.set_ylabel('y')
        self.ax.yaxis.label.set_color('green')
        self.ax.set_zlabel('z')
        self.ax.zaxis.label.set_color('blue')
        self.ax.set_title(self.name)
    def reset_position(self): # of the image plane axes
        self.tfmatrix = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]])
    def rotate_x(self,angle):
        self.tfmatrix = self.transformations.rotate_x_matrix(angle,self.tfmatrix)
    def rotate_y(self,angle):
        self.tfmatrix = self.transformations.rotate_y_matrix(angle,self.tfmatrix)
    def rotate_z(self,angle):
        self.tfmatrix = self.transformations.rotate_z_matrix(angle,self.tfmatrix)
    def translate_xyz(self,dx,dy,dz):
        self.tfmatrix = self.transformations.translate_xyz_matrix(dx,dy,dz,self.tfmatrix)
    # copfocalsxyz -> [copfocalx,copfocaly,copfocalz]
    def set_copfocalsxyz(self,copfocalsxyzlist):
        self.copfocalsxyz = copfocalsxyzlist