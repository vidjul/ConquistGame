

import numpy as np 

class Vertex:
    def __init__(self,key,size,color=-1):
        self.key = key
        self.size = size
        self.color = color
        self.soldiers = size
        self.connectedTo = {}

    def isNeighbor(self,vertex):
        return vertex in self.connectedTo

    def addNeighbor(self,key,weight=0):
        self.connectedTo[key] = weight

    def __str__(self):
        return str(self.key) + ' connectedTo : ' + str(self.getConnectionsKeys()) + ' & Color : '+str(self.color) + ' & soldier are : '+str(self.soldiers)

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getConnectionsKeys(self):
        return [x.key for x in self.getConnections()]

    def getWeight(self,key):
        if nbr in self.connectedTo:
            return self.connectedTo[key]
        else :
            return None
        
    def moveSoldiersToHome(self,goalVertex,soldierNumber):
        if goalVertex in self.getConnections():
            if self.soldiers >= soldierNumber :
                self.soldiers -= soldierNumber
                goalVertex.soldiers += soldierNumber
            else : 
                goalVertex.soldiers += self.soldiers
                self.soldiers = 0
            return True
        else :
            return False
                
    def moveSoldiersToWar(self,goalVertex,soldierNumber):
        if goalVertex in self.getConnections():
            if self.soldiers >= soldierNumber :
                self.soldiers -= soldierNumber
                goalVertex.soldiers -= soldierNumber
                if goalVertex.soldiers < 0 :
                    goalVertex.color = self.color
                    goalVertex.soldiers *= -1
            else : 
                goalVertex.soldiers -= self.soldiers
                self.soldiers = 0
                if goalVertex.soldiers < 0 :
                    goalVertex.color = self.color
                    goalVertex.soldiers *= -1
            return True
        else :
            return False
    
    def moveSoldiers(self,goalVertex,soldierNumber):
        if self.color != -1:
            if self.color == goalVertex.color :
                return self.moveSoldiersToHome(goalVertex,soldierNumber)
            else:
                return self.moveSoldiersToWar(goalVertex,soldierNumber)
        
                    
    def updateSoldiers(self):
        if self.color != -1:
            self.soldiers+=self.size
            
    def updateEdges(self):
        if self.soldiers != 0:
            for item in self.connectedTo:
                self.connectedTo[item] = float(item.soldiers)/self.soldiers + item.size/5.0
        else :
             for item in self.connectedTo:
                self.connectedTo[item] = item.soldiers + item.size/5.0 

                
                
                
                


# In[182]:

class Graph:
    def __init__(self,firstPlayerBaseKey,secondPlayerBaseKey, interface = None):
        self.vertList = {}
        self.numVertices = 0
        self.firstPlayerBaseKey = firstPlayerBaseKey
        self.secondPlayerBaseKey = secondPlayerBaseKey
        self.interface = interface

    def addVertex(self,vertex):
        self.numVertices += 1
        self.vertList[vertex.key] = vertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self,key1,key2):
        if key1 in self.vertList and key2  in self.vertList:
            self.vertList[key1].addNeighbor(self.vertList[key2], self.vertList[key2].soldiers/self.vertList[key1].soldiers+self.vertList[key2].size/5)
            self.vertList[key2].addNeighbor(self.vertList[key1], self.vertList[key1].soldiers/self.vertList[key2].soldiers+self.vertList[key1].size/5)
    
    def updateEdges(self):
        for item in self.vertList:
            self.vertList[item].updateEdges()            
    
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def nextTurn(self):
        for key in self.vertList:
            self.vertList[key].updateSoldiers()
            
    def movingIa(self):
        self.updateEdges()
        wayToGo = self.findTheMoves()
        if(wayToGo[1].color == 0 ):
            wayToGo[0].moveSoldiers(wayToGo[1],2*wayToGo[0].size/3)
            for i in range(1,len(wayToGo)-1):
                if wayToGo[i].color == 0 and wayToGo[i+1].color == 0 :
                    wayToGo[i].moveSoldiers(wayToGo[i+1],wayToGo[i].soldiers)
                else:
                    wayToGo[i].moveSoldiers(wayToGo[i+1],wayToGo[i].soldiers)
                    break
        else : 
            wayToGo[0].moveSoldiers(wayToGo[1],2*wayToGo[0].size/3)

        
    def __str__(self):
        returning=''
        for vert in self.vertList:
            returning += str(self.vertList[vert]) + '\n'
        return returning
    
    def getEdges(self):
        edges = {}
        for vertex in self.vertList :
            for neighbor in self.vertList[vertex].connectedTo:
                edges[(self.vertList[vertex],neighbor)] = self.vertList[vertex].connectedTo[neighbor]
        return edges
    
    def findTheMoves(self):
        return self.findPath(self.vertList.values(),self.getEdges(),self.vertList[self.firstPlayerBaseKey] ,self.vertList[self.secondPlayerBaseKey])
    
    def use_Bellman_Ford(self,vertices,edges,firstVertex):#edges is a dictionary with keys are like (u,v) where u and v the vertices
        dist = {}
        pred = {}
        for vertex in vertices :
            dist[vertex] = np.infty
            pred[vertex] = -1
        dist[firstVertex] = 0
        for  i in range(len(vertices)):
            for edge in edges :
                newLen = dist[edge[0]]+edges[edge]
                if newLen < dist[edge[1]]:
                    if i > len(vertices):
                        print 'negative cycle'
                        break
                    dist[edge[1]] = newLen
                    pred[edge[1]] = edge[0]
        return dist,pred    

    def findPath(self,vertices,edges,firstVertex,lastVertex):
        dist,pred=self.use_Bellman_Ford(vertices,edges,firstVertex)
        path = [lastVertex]
        while path[0] != firstVertex:
            path = [pred[lastVertex]] + path
            lastVertex = path[0]
        return path
    
    def gameOver(self) :
        return self.vertList[self.firstPlayerBaseKey].color == self.vertList[self.secondPlayerBaseKey].color

    def setToOneVOne(self):
        self.vertList[self.firstPlayerBaseKey].color=1
        self.vertList[self.secondPlayerBaseKey].color=2
    def setToOneVAI(self):
        self.vertList[self.firstPlayerBaseKey].color=0
        self.vertList[self.secondPlayerBaseKey].color=1

        
        



class Platforms:
    def __init__(self):
        self.games = {}
        self.numberOfGraphs = 0
    
    def addGame(self,graph,name):
        self.games[name] = graph
        self.numberOfGraphs += 1
    

    




