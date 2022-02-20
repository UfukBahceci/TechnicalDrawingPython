import numpy as np
import math
class Transformations:
    def __init__(self):
        pass
    def aligntonewbasebyrotatingZYZ_phi_theta_psi(self,rotationmatrix):
        Xx = rotationmatrix[0][0]
        Xy = rotationmatrix[1][0]
        Xz = rotationmatrix[2][0]
        Yx = rotationmatrix[0][1]
        Yy = rotationmatrix[1][1]
        Yz = rotationmatrix[2][1]
        Zx = rotationmatrix[0][2]
        Zy = rotationmatrix[1][2]
        Zz = rotationmatrix[2][2]
        phi = 0
        theta = 0
        psi = 0
        # a for cos(phi), b for sin(phi)
        # c for cos(theta), d for sin(theta)
        # e for cos(psi), f for sin(psi)
        theta = math.acos(Zz) # [0,Pi]     
        if Zz == 1:
            phi = 0
            psi = math.acos(Xx)
            if Xy < 0:
                psi = 2*math.pi-psi 
        elif Zz == -1:
            phi = 0
            psi = math.acos(-Xx)
            if Xy < 0:
                psi = 2*math.pi-psi
        else:
            d = math.sin(theta)
            psi = math.acos(-Xz/d)
            if (Yz/d) < 0:
                psi = 2*math.pi-psi
            phi = math.acos(Zx/d)
            if (Zy/d) < 0:
                phi = 2*math.pi-phi
        return [phi,theta,psi]
    def aligntoZbyrotatingYZ_theta_psi(self,vector):
        vectornorm2 = self.norm2_vector(vector)
        Vx = vector[0]
        Vy = vector[1]
        Vz = vector[2]
        if Vx == 0:
            psi = math.pi/2 # -Pi/2 or Pi/2
        else:
            psi = math.atan(-Vy/Vx) # [-Pi/2,Pi/2]
        if Vz == 0:
            costheta = 0 # -Pi/2 or Pi/2
            sintheta = -vectornorm2/(math.cos(psi)*Vx-math.sin(psi)*Vy)
            if sintheta > 0:
                theta = math.pi/2
            else:
                theta = -math.pi/2
        else:
            costheta = Vz/vectornorm2
            tantheta = -(math.cos(psi)*Vx-math.sin(psi)*Vy)/Vz
            theta = math.acos(costheta) # [0,Pi]
            if costheta >= 0: # [-Pi/2,Pi/2]
                if tantheta >= 0: # [0,Pi/2]
                    pass
                else: # [-Pi/2,0[
                    theta=-theta
            else: # ]Pi/2,3*Pi/2[
                if tantheta >= 0: # [Pi,3*Pi/2[
                    theta=2*math.pi-theta
                else: # ]Pi/2,Pi[
                    pass
        return [theta,psi]
    def reverse_direction(self,dvector):
        revdvector=np.array([-dvector[0],-dvector[1],-dvector[2],1])
        return revdvector
    def calculate_directionfrompoint1topoint2(self,vector1,vector2):
        direction=self.normalize_vector(vector2-vector1)       
        return direction
    def calculate_planenormalfromthreepoints(self,vector1,vector2,vector3):
        normal=self.cross_vectors(vector1-vector2,vector3-vector2)
        normal=self.normalize_vector(normal)
        return normal
    def project_vector2_on_vector1(self,vector2,vector1):
        projvectoronvector1 = (self.dot_vectors(vector2,vector1)/self.dot_vectors(vector1,vector1))*vector1
        projvectoronvector1 [3]=1
        return projvectoronvector1 
    def project_vector_on_plane(self,vector,planenormal):
        normalized_planenormal=planenormal/self.norm2_vector(planenormal)
        projvectoronplane = vector-(self.dot_vectors(vector,normalized_planenormal)*normalized_planenormal)
        projvectoronplane[3]=1
        return projvectoronplane
    def closestpointonlinetoorigin(self,linepoint,linedirection):
        projlinepointonlinedirection=self.project_vector2_on_vector1(linepoint,linedirection)
        closestpointonlinetoorigin=linepoint-projlinepointonlinedirection
        closestpointonlinetoorigin[3]=1
        return closestpointonlinetoorigin   
    def closestpointonlinetoanotherpoint(self,linepoint,linedirection,anotherpoint):
        closestpointonlinetoanotherpoint=linepoint+self.project_vector2_on_vector1((anotherpoint-linepoint),linedirection)
        closestpointonlinetoanotherpoint[3]=1
        return closestpointonlinetoanotherpoint 
    def closestpointonplanetoorigin(self,planepoint,planenormal):
        closestpointonplanetoorigin=planenormal*((self.dot_vectors(planepoint,planenormal))/(self.norm2_vector(planenormal)**2))
        closestpointonplanetoorigin[3]=1
        return closestpointonplanetoorigin
    def closestpointonplanetoanotherpoint(self,planepoint,planenormal,anotherpoint):
        closestpointonplanetoanotherpoint=anotherpoint+self.project_vector2_on_vector1((planepoint-anotherpoint),planenormal)
        closestpointonplanetoanotherpoint[3]=1
        return closestpointonplanetoanotherpoint
    # angle in radians (math.pi)
    def rotate_x_vector(self,angle,vector):
        #rotationmatrix_x = np.array([[1,0,0,0],[0,math.cos(angle),-math.sin(angle),0],[0,math.sin(angle),math.cos(angle),0],[0,0,0,1]]) 
        #return np.dot(rotationmatrix_x,vector)
        c=math.cos(angle)
        d=math.sin(angle)
        return np.array([vector[0],c*vector[1]-d*vector[2],d*vector[1]+c*vector[2],vector[3]])
    def rotate_x_matrix(self,angle,matrix):
        #rotationmatrix_x = np.array([[1,0,0,0],[0,math.cos(angle),-math.sin(angle),0],[0,math.sin(angle),math.cos(angle),0],[0,0,0,1]]) 
        #return rotationmatrix_x.dot(matrix)
        c=math.cos(angle)
        d=math.sin(angle)
        rmatrix=np.array([matrix[0][0],c*matrix[1][0]-d*matrix[2][0],d*matrix[1][0]+c*matrix[2][0],matrix[3][0]])
        for i in range(1,4):
            rmatrix=np.column_stack([rmatrix,np.array([matrix[0][i],c*matrix[1][i]-d*matrix[2][i],d*matrix[1][i]+c*matrix[2][i],matrix[3][i]])])
        return rmatrix
    def rotate_y_vector(self,angle,vector):
        #rotationmatrix_y = np.array([[math.cos(angle),0,math.sin(angle),0],[0,1,0,0],[-math.sin(angle),0,math.cos(angle),0],[0,0,0,1]]) 
        #return np.dot(rotationmatrix_y,vector)
        c=math.cos(angle)
        d=math.sin(angle)
        return np.array([c*vector[0]+d*vector[2],vector[1],-d*vector[0]+c*vector[2],vector[3]])
    def rotate_y_matrix(self,angle,matrix):
        #rotationmatrix_y = np.array([[math.cos(angle),0,math.sin(angle),0],[0,1,0,0],[-math.sin(angle),0,math.cos(angle),0],[0,0,0,1]]) 
        #return rotationmatrix_y.dot(matrix)
        c=math.cos(angle)
        d=math.sin(angle)
        rmatrix=np.array([c*matrix[0][0]+d*matrix[2][0],matrix[1][0],-d*matrix[0][0]+c*matrix[2][0],matrix[3][0]])
        for i in range(1,4):
            rmatrix=np.column_stack([rmatrix,np.array([c*matrix[0][i]+d*matrix[2][i],matrix[1][i],-d*matrix[0][i]+c*matrix[2][i],matrix[3][i]])])
        return rmatrix
    def rotate_z_vector(self,angle,vector):
        #rotationmatrix_z = np.array([[math.cos(angle),-math.sin(angle),0,0],[math.sin(angle),math.cos(angle),0,0],[0,0,1,0],[0,0,0,1]]) 
        #return np.dot(rotationmatrix_z,vector)
        c=math.cos(angle)
        d=math.sin(angle)
        return np.array([c*vector[0]-d*vector[1],d*vector[0]+c*vector[1],vector[2],vector[3]])      
    def rotate_z_matrix(self,angle,matrix):
        #rotationmatrix_z = np.array([[math.cos(angle),-math.sin(angle),0,0],[math.sin(angle),math.cos(angle),0,0],[0,0,1,0],[0,0,0,1]]) 
        #return rotationmatrix_z.dot(matrix)
        c=math.cos(angle)
        d=math.sin(angle)
        rmatrix=np.array([c*matrix[0][0]-d*matrix[1][0],d*matrix[0][0]+c*matrix[1][0],matrix[2][0],matrix[3][0]])
        for i in range(1,4):
             rmatrix=np.column_stack([rmatrix,np.array([c*matrix[0][i]-d*matrix[1][i],d*matrix[0][i]+c*matrix[1][i],matrix[2][i],matrix[3][i]])])
        return rmatrix
    def translate_xyz_vector(self,dx,dy,dz,vector):
        #translatematrix = np.array([[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]]) 
        #return np.dot(translatematrix,vector)      
        return np.array([vector[0]+dx*vector[3],vector[1]+dy*vector[3],vector[2]+dz*vector[3],vector[3]])
    def translate_xyz_matrix(self,dx,dy,dz,matrix):
        #translatematrix = np.array([[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]]) 
        #return translatematrix.dot(matrix)
        rmatrix=np.array([matrix[0][0]+dx*matrix[3][0],matrix[1][0]+dy*matrix[3][0],matrix[2][0]+dz*matrix[3][0],matrix[3][0]])
        for i in range(1,4):
             rmatrix=np.column_stack([rmatrix,np.array([matrix[0][i]+dx*matrix[3][i],matrix[1][i]+dy*matrix[3][i],matrix[2][i]+dz*matrix[3][i],matrix[3][i]])])
        return rmatrix        
    def norm2_vector(self,vector):
        return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    def normalize_vector(self,vector):
        nvector=vector/self.norm2_vector(vector)
        nvector[3]=1
        return nvector
    def homogenproject_vector(self,vector):
        h=0.+vector[3]
        hvector=vector/h
        hvector[3]=1
        return hvector
    def dot_vectors(self,vector1,vector2):
        return vector1[0]*vector2[0]+vector1[1]*vector2[1]+vector1[2]*vector2[2]
    def cross_vectors(self,vector1,vector2):
        crossproductvector = np.array([vector1[1]*vector2[2]-vector2[1]*vector1[2],vector2[0]*vector1[2]-vector1[0]*vector2[2],vector1[0]*vector2[1]-vector2[0]*vector1[1],1])
        return crossproductvector