class Edge:
    def __init__(self,fromvertex,tovertex):
        self.fromvertex = fromvertex
        self.tovertex = tovertex
    def refresh(self):
        self.tracepointlist = []
        for index in range(len(self.fromvertex.obj.scene.cameralist)):
            self.tracepointlist.append([])
    def settracepointwrcam(self,tracepointvect,index):
        self.tracepointlist[index].append(tracepointvect)
    def gettracepointwrcam(self,index):
        return self.tracepointlist[index][0]