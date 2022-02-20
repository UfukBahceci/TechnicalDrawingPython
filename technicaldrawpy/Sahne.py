import matplotlib.pyplot as plt
import numpy as np
from technicaldrawpy.Transformations import *
class Sahne:
    def __init__(self,azim,dist,elev): # azimuth angle, distance, elevation angle
        self.numberofcams = 0
        self.fig = plt.figure(figsize=(9,6),dpi=100)
        self.ax = self.fig.add_subplot(self.numberofcams+1,1,1,projection='3d')
        self.ax.azim = azim
        self.ax.dist = dist
        self.ax.elev = elev
        self.tf = Transformations()
        self.copdistancelimit = 5 # do not show if the center of projection is too far from the image plane center
        self.clear()
    def clear(self):
        self.ax.clear()
        self.ax.set_xlabel('x')
        self.ax.xaxis.label.set_color('red')
        self.ax.set_ylabel('y')
        self.ax.yaxis.label.set_color('green')
        self.ax.set_zlabel('z')
        self.ax.zaxis.label.set_color('blue')
    def addbaseaxes(self): #
        self.borijin_vect = np.array([0,0,0,1])
        self.bxaxis_vect = np.array([1,0,0,1])
        self.byaxis_vect = np.array([0,1,0,1])
        self.bzaxis_vect = np.array([0,0,1,1])
    def addnewaxes(self): #
        self.norijin_vect = np.array([0,0,0,1])
        self.nxaxis_vect = np.array([1,0,0,1])
        self.nyaxis_vect = np.array([0,1,0,1])
        self.nzaxis_vect = np.array([0,0,1,1])
    # angle in radians (math.pi)
    def rotate_x_newaxes(self,angle):
        self.norijin_vect = self.tf.rotate_x_vector(angle,self.norijin_vect)
        self.nxaxis_vect = self.tf.rotate_x_vector(angle,self.nxaxis_vect)
        self.nyaxis_vect = self.tf.rotate_x_vector(angle,self.nyaxis_vect)
        self.nzaxis_vect = self.tf.rotate_x_vector(angle,self.nzaxis_vect)
    def rotate_y_newaxes(self,angle):
        self.norijin_vect = self.tf.rotate_y_vector(angle,self.norijin_vect)
        self.nxaxis_vect = self.tf.rotate_y_vector(angle,self.nxaxis_vect)
        self.nyaxis_vect = self.tf.rotate_y_vector(angle,self.nyaxis_vect)
        self.nzaxis_vect = self.tf.rotate_y_vector(angle,self.nzaxis_vect)
    def rotate_z_newaxes(self,angle):
        self.norijin_vect = self.tf.rotate_z_vector(angle,self.norijin_vect)
        self.nxaxis_vect = self.tf.rotate_z_vector(angle,self.nxaxis_vect)
        self.nyaxis_vect = self.tf.rotate_z_vector(angle,self.nyaxis_vect)
        self.nzaxis_vect = self.tf.rotate_z_vector(angle,self.nzaxis_vect)
    def translate_xyz_newaxes(self,dx,dy,dz):
        self.norijin_vect = self.tf.translate_xyz_vector(dx,dy,dz,self.norijin_vect)
        self.nxaxis_vect = self.tf.translate_xyz_vector(dx,dy,dz,self.nxaxis_vect)
        self.nyaxis_vect = self.tf.translate_xyz_vector(dx,dy,dz,self.nyaxis_vect)
        self.nzaxis_vect = self.tf.translate_xyz_vector(dx,dy,dz,self.nzaxis_vect)
    def show(self):
        maxx=max(self.ax.get_xlim())
        maxy=max(self.ax.get_ylim())
        maxz=max(self.ax.get_zlim())
        minx=min(self.ax.get_xlim())
        miny=min(self.ax.get_ylim())
        minz=min(self.ax.get_zlim())        
        maxoflimits = max(max(maxx,maxy),maxz)
        minoflimits = min(min(minx,miny),minz)
        self.ax.set_xlim(minoflimits-0.5,maxoflimits+0.5)
        self.ax.set_ylim(minoflimits-0.5,maxoflimits+0.5)
        self.ax.set_zlim(minoflimits-0.5,maxoflimits+0.5)
    def show_vector(self,vector,color):
        self.ax.scatter(vector[0],vector[1],vector[2],marker='o',color=color)
        self.ax.quiver(0,0,0,vector[0],vector[1],vector[2],color=color,alpha=0.8,lw=3)
    def show_line(self,point,direction):
        # dogru denklemi: [x,y,z]=[pointx,pointy,pointz]+t[a,b,c], [a,b,c] dogrunun yon vektoru ve t reel sayi
        maxx=max(self.ax.get_xlim())
        maxy=max(self.ax.get_ylim())
        maxz=max(self.ax.get_zlim())
        minx=min(self.ax.get_xlim())
        miny=min(self.ax.get_ylim())
        minz=min(self.ax.get_zlim())        
        maxoflimits=max(max(maxx,maxy),maxz)
        minoflimits=min(min(minx,miny),minz)
        x=np.linspace(minoflimits*0.9,maxoflimits*0.9,2)
        direction=direction/self.tf.norm2_vector(direction)
        t=(x-point[0])/direction[0]
        y=(direction[1]*t)+point[1]
        z=(direction[2]*t)+point[2]
        self.ax.plot(x,y,z)
    def show_plane(self,point,normal):
        # düzlem denklemi: a*x+b*y+c*z+d=0, [a,b,c] duzleme normal vektor
        if normal[2]!=0:           
            maxx=max(self.ax.get_xlim())
            maxy=max(self.ax.get_ylim())
            maxz=max(self.ax.get_zlim())
            minx=min(self.ax.get_xlim())
            miny=min(self.ax.get_ylim())
            minz=min(self.ax.get_zlim())        
            minoflimits=min(min(minx,miny),minz)
            maxoflimits=max(max(maxx,maxy),maxz)
            d=-self.tf.dot_vectors(point,normal)
            x=np.linspace(minoflimits*0.9,maxoflimits*0.9,2)
            y=np.linspace(minoflimits*0.9,maxoflimits*0.9,2)
            X,Y=np.meshgrid(x,y)
            Z=(-normal[0]*X-normal[1]*Y-d)/normal[2]
            self.ax.plot_surface(X,Y,Z,alpha=0.2)
    def show_baseaxes(self):
        self.ax.scatter(self.bxaxis_vect[0],self.bxaxis_vect[1],self.bxaxis_vect[2],marker='o',color="red",alpha=0.3)
        self.ax.scatter(self.byaxis_vect[0],self.byaxis_vect[1],self.byaxis_vect[2],marker='o',color="green",alpha=0.3)
        self.ax.scatter(self.bzaxis_vect[0],self.bzaxis_vect[1],self.bzaxis_vect[2],marker='o',color="blue",alpha=0.3)
        self.ax.quiver(self.borijin_vect[0],self.borijin_vect[1],self.borijin_vect[2],self.bxaxis_vect[0]-self.borijin_vect[0],self.bxaxis_vect[1]-self.borijin_vect[1],self.bxaxis_vect[2]-self.borijin_vect[2],color='red',alpha=0.1,lw=3)
        self.ax.quiver(self.borijin_vect[0],self.borijin_vect[1],self.borijin_vect[2],self.byaxis_vect[0]-self.borijin_vect[0],self.byaxis_vect[1]-self.borijin_vect[1],self.byaxis_vect[2]-self.borijin_vect[2],color='green',alpha=0.1,lw=3)
        self.ax.quiver(self.borijin_vect[0],self.borijin_vect[1],self.borijin_vect[2],self.bzaxis_vect[0]-self.borijin_vect[0],self.bzaxis_vect[1]-self.borijin_vect[1],self.bzaxis_vect[2]-self.borijin_vect[2],color='blue',alpha=0.1,lw=3)
    def show_newaxes(self):
        self.ax.scatter(self.nxaxis_vect[0],self.nxaxis_vect[1],self.nxaxis_vect[2],marker='o',color="red")
        self.ax.scatter(self.nyaxis_vect[0],self.nyaxis_vect[1],self.nyaxis_vect[2],marker='o',color="green")
        self.ax.scatter(self.nzaxis_vect[0],self.nzaxis_vect[1],self.nzaxis_vect[2],marker='o',color="blue")
        self.ax.quiver(self.norijin_vect[0],self.norijin_vect[1],self.norijin_vect[2],self.nxaxis_vect[0]-self.norijin_vect[0],self.nxaxis_vect[1]-self.norijin_vect[1],self.nxaxis_vect[2]-self.norijin_vect[2],color='red',alpha=0.8,lw=3)
        self.ax.quiver(self.norijin_vect[0],self.norijin_vect[1],self.norijin_vect[2],self.nyaxis_vect[0]-self.norijin_vect[0],self.nyaxis_vect[1]-self.norijin_vect[1],self.nyaxis_vect[2]-self.norijin_vect[2],color='green',alpha=0.8,lw=3)
        self.ax.quiver(self.norijin_vect[0],self.norijin_vect[1],self.norijin_vect[2],self.nzaxis_vect[0]-self.norijin_vect[0],self.nzaxis_vect[1]-self.norijin_vect[1],self.nzaxis_vect[2]-self.norijin_vect[2],color='blue',alpha=0.8,lw=3)