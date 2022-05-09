import sys
#sys.path.append("<InstallPath>\TechnicalDrawingPython")

import numpy as np
import math

from mpl_toolkits import mplot3d # required for Matplotlib < 3.2.0
from technicaldrawpy import Transformations,Sahne,Camera,Vertex,Edge,Surface,LinearObject,Cube,Sahnecams

import matplotlib
print("Matplotlib version:")
print(matplotlib.__version__)

print("interactive backends:")
print(matplotlib.rcsetup.interactive_bk)
print("non-interactive backends:")
print(matplotlib.rcsetup.non_interactive_bk)
matplotlib.use('WebAgg')

scene_01=Sahnecams.Sahnecams(35,6,15,"Main Scene\n",3) # 3 cameras are defined
scene_01.copdistancelimit=5 # do not show the center of projection if it is more than 5 units away from O 
mycam1=Camera.Camera(-135,6,15,scene_01,"Perspective Projection z",None)
mycam1.set_copfocalsxyz([-1000000,-1000000,-4]) # -1000000 (at infinity)
# set_generateviewbools(cameratfgen,persorobliquetfgen,prjztfgen,traceptgen,vrfraypersgen,vrfrayobliquegen)
mycam1.set_generateviewbools(True,False,True,False,True,False)
mycam2=Camera.Camera(-135,6,15,scene_01,"Perspective Transformation z",[-2,2]) # [-2,2] view limits
mycam2.set_copfocalsxyz([-1000000,-1000000,-4]) # -1000000 (at infinity)
mycam2.set_generateviewbools(False,True,True,False,False,False)
mycam3=Camera.Camera(90,8,-90,scene_01,"Projection Plane",[-2,2])
mycam3.set_copfocalsxyz([-1000000,-1000000,-4]) # -1000000 (at infinity)
mycam3.set_generateviewbools(False,False,True,False,False,False)
scene_01.addcamera(mycam1)
scene_01.addcamera(mycam2)
scene_01.addcamera(mycam3)
mycube=Cube.Cube(4,4,3,scene_01,"Cube") # a cube object of size 4 x 4 x 3
mycube.translate_xyz(0,0,3)
scene_01.addobj(mycube)
scene_01.calculate_positions()
scene_01.show()
mycam3.ax.invert_xaxis()

matplotlib.pyplot.show()
