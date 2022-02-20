from technicaldrawpy.Sahne import *
class Sahnecams(Sahne):
    def __init__(self,azim,dist,elev,name,numberofcams):
        self.numberofcams = numberofcams
        self.currentcamindex = 1
        self.fig = plt.figure(figsize=(9,(self.numberofcams+1)*6),dpi=100)
        self.fig.suptitle(" ",fontsize=12)
        plt.subplots_adjust(wspace=0.25,hspace=1)
        self.ax = self.fig.add_subplot(self.numberofcams+1,1,1,projection='3d')
        self.name = name
        self.ax.azim = azim
        self.ax.dist = dist
        self.ax.elev = elev
        self.tf = Transformations()
        self.copdistancelimit = 5 # do not show if the center of projection is too far from the image plane center
        self.cameralist = []
        self.objlist = []
        self.clear()
    def clear(self):
        super().clear()
        for c in self.cameralist:
            c.clear()
        for o in self.objlist:
            o.refresh()
        self.ax.set_title(self.name)
    def addcamera(self,camobj):
        self.cameralist.append(camobj)
        camobj.clear()
        for o in self.objlist:
            o.refresh()
    def addobj(self,obj):
        self.objlist.append(obj)
        obj.refresh()
    def calculate_positions_oblique(self,beta,alpha):
        for o in self.objlist:
            for index in range(len(self.cameralist)):
                o.calculate_positionwrcam(index)
                o.calculate_obliquetransformation(index,beta,alpha)
                o.calculate_projectionz(index) 
    def calculate_positions(self):
        for o in self.objlist:
            for index in range(len(self.cameralist)):
                o.calculate_positionwrcam(index)
                o.calculate_perspectivetransformation(index)
                o.calculate_projectionz(index)
    def generate_views(self):
        self.ax.text(0,0,0.1,"O",color='black')
        self.ax.scatter(0,0,0,marker='o',color='black')        
        for c in self.cameralist:
            orijin=np.array([0.,0.,0.,1.])
            xaxis=np.array([1.,0.,0.,1.])
            yaxis=np.array([0.,1.,0.,1.])
            zaxis=np.array([0.,0.,1.,1.])
            tforijin=np.dot(c.tfmatrix,orijin)
            tfxaxis=np.dot(c.tfmatrix,xaxis)
            tfyaxis=np.dot(c.tfmatrix,yaxis)
            tfzaxis=np.dot(c.tfmatrix,zaxis)
            self.ax.text(tforijin[0],tforijin[1],tforijin[2]+1,c.name,color='black')
            self.ax.scatter(tforijin[0],tforijin[1],tforijin[2],marker='o',color='black')
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfxaxis[0]-tforijin[0],tfxaxis[1]-tforijin[1],tfxaxis[2]-tforijin[1],color='red',alpha=.7,lw=2)
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfyaxis[0]-tforijin[0],tfyaxis[1]-tforijin[1],tfyaxis[2]-tforijin[1],color='green',alpha=.7,lw=2)
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfzaxis[0]-tforijin[0],tfzaxis[1]-tforijin[1],tfzaxis[2]-tforijin[1],color='blue',alpha=.7,lw=2)           
        for o in self.objlist:
            orijin=np.array([0.,0.,0.,1.])
            xaxis=np.array([1.,0.,0.,1.])
            yaxis=np.array([0.,1.,0.,1.])
            zaxis=np.array([0.,0.,1.,1.])
            tforijin=np.dot(o.tfmatrix,orijin)
            tfxaxis=np.dot(o.tfmatrix,xaxis)
            tfyaxis=np.dot(o.tfmatrix,yaxis)
            tfzaxis=np.dot(o.tfmatrix,zaxis)
            self.ax.text(tforijin[0],tforijin[1],tforijin[2]+1,o.name,color='black')
            self.ax.scatter(tforijin[0],tforijin[1],tforijin[2],marker='o',color='black')
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfxaxis[0]-tforijin[0],tfxaxis[1]-tforijin[1],tfxaxis[2]-tforijin[2],color='red',alpha=.7,lw=2)
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfyaxis[0]-tforijin[0],tfyaxis[1]-tforijin[1],tfyaxis[2]-tforijin[2],color='green',alpha=.7,lw=2)
            self.ax.quiver(tforijin[0],tforijin[1],tforijin[2],tfzaxis[0]-tforijin[0],tfzaxis[1]-tforijin[1],tfzaxis[2]-tforijin[2],color='blue',alpha=.7,lw=2)
        for o in self.objlist:
            for index in range(len(self.cameralist)):
                if self.cameralist[index].cameratfgen == True:
                    o.generate_camtf3Dview(index)
                if self.cameralist[index].persorobliquetfgen == True:
                    o.generate_perstf3Dview(index)
                if self.cameralist[index].prjztfgen == True:
                    o.generate_prjztf3Dview(index)
                o.generate_imageplanez(index)
                if self.cameralist[index].traceptgen == True:
                    o.generate_verificationraystracepoints(index)
                if self.cameralist[index].vrfraypersgen == True:
                    o.generate_verificationrayspersprjz(index)
                if self.cameralist[index].vrfrayobliquegen == True:
                    o.generate_verificationraysobliqueprjz(index)
    def show(self):
        self.generate_views()
        super().show()
        for c in self.cameralist:
            maxx=max(c.ax.get_xlim())
            maxy=max(c.ax.get_ylim())
            maxz=max(c.ax.get_zlim())
            minx=min(c.ax.get_xlim())
            miny=min(c.ax.get_ylim())
            minz=min(c.ax.get_zlim())        
            maxoflimits = max(max(maxx,maxy),maxz)
            minoflimits = min(min(minx,miny),minz)
            c.ax.set_xlim(minoflimits-0.5,maxoflimits+0.5)
            c.ax.set_ylim(minoflimits-0.5,maxoflimits+0.5)
            c.ax.set_zlim(minoflimits-0.5,maxoflimits+0.5)