import numpy as np
import math
class LinearObject:
    def __init__(self,sceneobj,name):
        self.reset_position()
        self.name=name
        self.scene = sceneobj
        self.transformations = sceneobj.tf
    def refresh(self):
        self.orijin.refresh()
        for v in self.vertexlist:
            v.refresh()
        for e in self.edgelist:
            e.refresh()
        for s in self.surfacelist:
            s.refresh()
    def reset_position(self):
        self.tfmatrix = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]])
    def rotate_x(self,angle):
        self.tfmatrix = self.transformations.rotate_x_matrix(angle,self.tfmatrix)
    def rotate_y(self,angle):
        self.tfmatrix = self.transformations.rotate_y_matrix(angle,self.tfmatrix)
    def rotate_z(self,angle):
        self.tfmatrix = self.transformations.rotate_z_matrix(angle,self.tfmatrix)
    def translate_xyz(self,dx,dy,dz):
        self.tfmatrix = self.transformations.translate_xyz_matrix(dx,dy,dz,self.tfmatrix)
    def calculate_positionwrcam(self,index):
        camobj=self.scene.cameralist[index]
        tfmatrixwrcam = np.linalg.inv(camobj.tfmatrix).dot(self.tfmatrix)
        for v in self.vertexlist:
            v.setpositionwrcam(np.dot(tfmatrixwrcam,v.positionwrobj),index)
        self.orijin.setpositionwrcam(np.dot(tfmatrixwrcam,self.orijin.positionwrobj),index)
        for s in self.surfacelist:
            s.calculate_normal(self,index)
            s.calculate_unrealisticshadingintensity(self,index)
    def calculate_perspectivetransformation(self,index):
        camobj=self.scene.cameralist[index]
        perstfmatrix = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[-1/camobj.copfocalsxyz[0],-1/camobj.copfocalsxyz[1],-1/camobj.copfocalsxyz[2],1]])
        for v in self.vertexlist:
            v.setpositionperstfwrcam(self.transformations.homogenproject_vector(np.dot(perstfmatrix,v.getpositionwrcam(index))),index)
        self.orijin.setpositionperstfwrcam(self.transformations.homogenproject_vector(np.dot(perstfmatrix,self.orijin.getpositionwrcam(index))),index)
    def calculate_obliquetransformation(self,index,beta,alpha):
        camobj=self.scene.cameralist[index]
        obliquetfmatrix = np.array([[1.,0.,math.tan(beta)*math.cos(alpha),0.],[0.,1.,math.tan(beta)*math.sin(alpha),0.],[0.,0.,1.,0.],[0,0,0,1]])
        for v in self.vertexlist:
            v.setpositionperstfwrcam(self.transformations.homogenproject_vector(np.dot(obliquetfmatrix,v.getpositionwrcam(index))),index)
        self.orijin.setpositionperstfwrcam(self.transformations.homogenproject_vector(np.dot(obliquetfmatrix,self.orijin.getpositionwrcam(index))),index)    
    def calculate_projectionz(self,index):
        camobj=self.scene.cameralist[index]
        prjzmatrix = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,1.]])
        for v in self.vertexlist:
            v.setpositionprjztfwrcam(np.dot(prjzmatrix,v.getpositionperstfwrcam(index)),index)
        self.orijin.setpositionprjztfwrcam(np.dot(prjzmatrix,self.orijin.getpositionperstfwrcam(index)),index)
    def generate_camtf3Dview(self,index):
        camobj=self.scene.cameralist[index]
        for v in self.vertexlist:
            camobj.ax.scatter(v.getpositionwrcam(index)[0],v.getpositionwrcam(index)[1],v.getpositionwrcam(index)[2],marker='x',color='black')
        for s in self.surfacelist:
            s.generate_planecoordinateswrcam(index)
            if s.getunrealisticshadingintensity(index)[0] > 0:
                camobj.ax.plot_surface(s.getplaneXwrcam(index),s.getplaneYwrcam(index),s.getplaneZwrcam(index),alpha=0.5,color=str(s.getunrealisticshadingintensity(index)[0]))
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] <= 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionwrcam(index)[0],e.tovertex.getpositionwrcam(index)[0]],[e.fromvertex.getpositionwrcam(index)[1],e.tovertex.getpositionwrcam(index)[1]],[e.fromvertex.getpositionwrcam(index)[2],e.tovertex.getpositionwrcam(index)[2]],'gray',alpha=.5)
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] > 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionwrcam(index)[0],e.tovertex.getpositionwrcam(index)[0]],[e.fromvertex.getpositionwrcam(index)[1],e.tovertex.getpositionwrcam(index)[1]],[e.fromvertex.getpositionwrcam(index)[2],e.tovertex.getpositionwrcam(index)[2]],'black')
    def generate_perstf3Dview(self,index):
        camobj=self.scene.cameralist[index]
        for v in self.vertexlist:
            camobj.ax.scatter(v.getpositionperstfwrcam(index)[0],v.getpositionperstfwrcam(index)[1],v.getpositionperstfwrcam(index)[2],marker='x',color='black')
        for s in self.surfacelist:
            s.generate_planecoordinatesperstfwrcam(index)
            if s.getunrealisticshadingintensity(index)[0] > 0:
                camobj.ax.plot_surface(s.getplaneXperstfwrcam(index),s.getplaneYperstfwrcam(index),s.getplaneZperstfwrcam(index),alpha=0.5,color=str(s.getunrealisticshadingintensity(index)[0]))
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] <= 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionperstfwrcam(index)[0],e.tovertex.getpositionperstfwrcam(index)[0]],[e.fromvertex.getpositionperstfwrcam(index)[1],e.tovertex.getpositionperstfwrcam(index)[1]],[e.fromvertex.getpositionperstfwrcam(index)[2],e.tovertex.getpositionperstfwrcam(index)[2]],'gray',alpha=.5)
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] > 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionperstfwrcam(index)[0],e.tovertex.getpositionperstfwrcam(index)[0]],[e.fromvertex.getpositionperstfwrcam(index)[1],e.tovertex.getpositionperstfwrcam(index)[1]],[e.fromvertex.getpositionperstfwrcam(index)[2],e.tovertex.getpositionperstfwrcam(index)[2]],'black')
    def generate_prjztf3Dview(self,index):
        camobj=self.scene.cameralist[index]
        for v in self.vertexlist:
            camobj.ax.scatter(v.getpositionprjztfwrcam(index)[0],v.getpositionprjztfwrcam(index)[1],v.getpositionprjztfwrcam(index)[2],marker='x',color='black')
        for s in self.surfacelist:
            s.generate_planecoordinatesprjztfwrcam(index)
            if s.getunrealisticshadingintensity(index)[0] > 0:
                camobj.ax.plot_surface(s.getplaneXprjztfwrcam(index),s.getplaneYprjztfwrcam(index),s.getplaneZprjztfwrcam(index),alpha=0.5,color=str(s.getunrealisticshadingintensity(index)[0]))
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] <= 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionprjztfwrcam(index)[0],e.tovertex.getpositionprjztfwrcam(index)[0]],[e.fromvertex.getpositionprjztfwrcam(index)[1],e.tovertex.getpositionprjztfwrcam(index)[1]],[e.fromvertex.getpositionprjztfwrcam(index)[2],e.tovertex.getpositionprjztfwrcam(index)[2]],'gray',alpha=.5)
        for s in self.surfacelist:
            if s.getunrealisticshadingintensity(index)[0] > 0:
                for e in s.edgeloop:
                    camobj.ax.plot3D([e.fromvertex.getpositionprjztfwrcam(index)[0],e.tovertex.getpositionprjztfwrcam(index)[0]],[e.fromvertex.getpositionprjztfwrcam(index)[1],e.tovertex.getpositionprjztfwrcam(index)[1]],[e.fromvertex.getpositionprjztfwrcam(index)[2],e.tovertex.getpositionprjztfwrcam(index)[2]],'black')
    def generate_imageplanez(self,index):
        camobj=self.scene.cameralist[index]
        camobj.ax.scatter(0,0,0,marker='o',color='black') # origin of the image plane
        if abs(camobj.copfocalsxyz[0])<self.scene.copdistancelimit:
            camobj.ax.scatter(camobj.copfocalsxyz[0],0,0,marker='o',color='red') # center of projection x
        if abs(camobj.copfocalsxyz[1])<self.scene.copdistancelimit:
            camobj.ax.scatter(0,camobj.copfocalsxyz[1],0,marker='o',color='green') # center of projection y
        if abs(camobj.copfocalsxyz[2])<self.scene.copdistancelimit:
            camobj.ax.scatter(0,0,camobj.copfocalsxyz[2],marker='o',color='blue') # center of projection z
        if camobj.viewlimits == None:
            maxx=max(camobj.ax.get_xlim())
            maxy=max(camobj.ax.get_ylim())
            maxz=max(camobj.ax.get_zlim())
            minx=min(camobj.ax.get_xlim())
            miny=min(camobj.ax.get_ylim())
            minz=min(camobj.ax.get_zlim())
            minoflimits=min(min(minx,miny),minz)
            maxoflimits=max(max(maxx,maxy),maxz)
            camobj.ax.quiver(0,0,minz,0,0,maxz,color='black',alpha=.3,lw=2)
            x=np.linspace(minoflimits*1.1,maxoflimits*1.1,2)
            y=np.linspace(minoflimits*1.1,maxoflimits*1.1,2)
            z=np.linspace(0,0,4)
            X,Y=np.meshgrid(x,y)
            Z=z.reshape(-1,2)
            #Z=np.reshape(z,X.shape)
            camobj.ax.plot_surface(X,Y,Z,alpha=0.1,color='blue')
            camobj.ax.set_xlim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_ylim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_zlim(minoflimits-0.5,maxoflimits+0.5)
        elif len(camobj.viewlimits) == 2:
            minoflimits=camobj.viewlimits[0]
            maxoflimits=camobj.viewlimits[1]
            #camobj.ax.quiver(0,0,minoflimits,0,0,maxoflimits,color='black',alpha=.3,lw=2)
            camobj.ax.set_xlim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_ylim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_zlim(minoflimits-0.5,maxoflimits+0.5)
        else:
            print("Please specify viewlimits for the ",camobj.name)
            minoflimits=1
            maxoflimits=1
            #camobj.ax.quiver(0,0,minoflimits,0,0,maxoflimits,color='black',alpha=.3,lw=2)
            camobj.ax.set_xlim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_ylim(minoflimits-0.5,maxoflimits+0.5)
            camobj.ax.set_zlim(minoflimits-0.5,maxoflimits+0.5)
    def generate_verificationraystracepoints(self,index):
        camobj=self.scene.cameralist[index]
        for e in self.edgelist:
            dx=e.tovertex.getpositionwrcam(index)[0]-e.fromvertex.getpositionwrcam(index)[0]
            dy=e.tovertex.getpositionwrcam(index)[1]-e.fromvertex.getpositionwrcam(index)[1]
            dz=e.tovertex.getpositionwrcam(index)[2]-e.fromvertex.getpositionwrcam(index)[2]
            dh=0
            if camobj.copfocalsxyz[0] > camobj.copfocalsxyzinfinity:
                dh=dh-(dx/camobj.copfocalsxyz[0])
            if camobj.copfocalsxyz[1] > camobj.copfocalsxyzinfinity:
                dh=dh-(dy/camobj.copfocalsxyz[1])
            if camobj.copfocalsxyz[2] > camobj.copfocalsxyzinfinity:
                dh=dh-(dz/camobj.copfocalsxyz[2])
            if abs(dh) > 0.0001:
                tracepoint=np.array([dx,dy,0.,dh])
                tracepoint=self.transformations.homogenproject_vector(tracepoint)
                e.settracepointwrcam(tracepoint,index)
                camobj.ax.scatter(tracepoint[0],tracepoint[1],tracepoint[2],marker='o',color='orange') # trace point (not at infinity)
                camobj.ax.plot3D([tracepoint[0],e.fromvertex.getpositionprjztfwrcam(index)[0]],[tracepoint[1],e.fromvertex.getpositionprjztfwrcam(index)[1]],[tracepoint[2],e.fromvertex.getpositionprjztfwrcam(index)[2]],'orange',alpha=.2)
                camobj.ax.plot3D([tracepoint[0],e.tovertex.getpositionprjztfwrcam(index)[0]],[tracepoint[1],e.tovertex.getpositionprjztfwrcam(index)[1]],[tracepoint[2],e.tovertex.getpositionprjztfwrcam(index)[2]],'orange',alpha=.2)
            else:
                tracepoint1=np.array([dx,dy,0,0]) # trace point (at infinity)
                tracepoint2=np.array([-dx,-dy,0,0]) # trace point (at infinity)
    def generate_verificationrayspersprjz(self,index):
        camobj=self.scene.cameralist[index]
        for v in self.vertexlist:
            camobj.ax.plot3D([0,v.getpositionwrcam(index)[0]],[0,v.getpositionwrcam(index)[1]],[camobj.copfocalsxyz[2],v.getpositionwrcam(index)[2]],'blue',alpha=.1)
    def generate_verificationraysobliqueprjz(self,index):
        camobj=self.scene.cameralist[index]
        for v in self.vertexlist:
            camobj.ax.plot3D([v.getpositionprjztfwrcam(index)[0],v.getpositionwrcam(index)[0]],[v.getpositionprjztfwrcam(index)[1],v.getpositionwrcam(index)[1]],[v.getpositionprjztfwrcam(index)[2],v.getpositionwrcam(index)[2]],'blue',alpha=.1)