from technicaldrawpy.Surface import *
from technicaldrawpy.Edge import *
from technicaldrawpy.Vertex import *
from technicaldrawpy.LinearObject import *
class Cube(LinearObject):
    def __init__(self,length,width,depth,sceneobj,name):
        super().__init__(sceneobj,name)
        self.orijin = Vertex(np.array([0.,0.,0.,1.]),self)
        self.length = length
        self.width= width
        self.depth = depth
        v1 = Vertex(np.array([-self.length/2,self.width/2,-self.depth/2,1]),self) # onsagust
        v2 = Vertex(np.array([-self.length/2,-self.width/2,-self.depth/2,1]),self) # onsagalt
        v3 = Vertex(np.array([self.length/2,-self.width/2,-self.depth/2,1]),self) # onsolalt
        v4 = Vertex(np.array([self.length/2,self.width/2,-self.depth/2,1]),self) # onsolust
        v5 = Vertex(np.array([-self.length/2,self.width/2,self.depth/2,1]),self) # arkasagust
        v6 = Vertex(np.array([-self.length/2,-self.width/2,self.depth/2,1]),self) # arkasagalt
        v7 = Vertex(np.array([self.length/2,-self.width/2,self.depth/2,1]),self) # arkasolalt
        v8 = Vertex(np.array([self.length/2,self.width/2,self.depth/2,1]),self) # arkasolust
        self.vertexlist = [v1,v2,v3,v4,v5,v6,v7,v8]
        e1 = Edge(v1,v2)
        e2 = Edge(v2,v3)
        e3 = Edge(v3,v4)
        e4 = Edge(v4,v1)
        e5 = Edge(v5,v6)
        e6 = Edge(v6,v7)
        e7 = Edge(v7,v8)
        e8 = Edge(v8,v5)
        e9 = Edge(v1,v5)
        e10 = Edge(v2,v6)
        e11 = Edge(v3,v7)
        e12 = Edge(v4,v8)
        self.edgelist = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]        
        s1 = Surface(self) #v1,v2,v3,v4
        s1.add_edge(e1)
        s1.add_edge(e2)
        s1.add_edge(e3)
        s1.add_edge(e4)
        s1.find_orderedvertexlist()
        s2 = Surface(self) #v5,v6,v7,v8
        s2.add_edge(e5)
        s2.add_edge(e6)
        s2.add_edge(e7)
        s2.add_edge(e8)
        s2.find_orderedvertexlist()
        s3 = Surface(self) #v1,v5,v6,v2
        s3.add_edge(e9)
        s3.add_edge(e5)
        s3.add_edge(e10)
        s3.add_edge(e1)
        s3.find_orderedvertexlist()
        s4 = Surface(self) #v3,v7,v8,v4
        s4.add_edge(e3)
        s4.add_edge(e11)
        s4.add_edge(e7)
        s4.add_edge(e12)
        s4.find_orderedvertexlist()
        s5 = Surface(self) #v2,v3,v7,v6
        s5.add_edge(e2)
        s5.add_edge(e11)
        s5.add_edge(e6)
        s5.add_edge(e10)
        s5.find_orderedvertexlist()
        s6 = Surface(self) #v1,v4,v8,v5
        s6.add_edge(e4)
        s6.add_edge(e12)
        s6.add_edge(e8)
        s6.add_edge(e9)
        s6.find_orderedvertexlist()
        self.surfacelist = [s1,s2,s3,s4,s5,s6]