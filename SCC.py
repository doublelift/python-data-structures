# Implementation of a graph using an adjacency list:

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # {key = Vertex object : value = int}

        self.discovered = None
        self.finished = None
        self.color = 'white'
        self.predecessor = None

    # getter and setter methods for additional properties:
    def setDiscovered(self, t):
        self.discovered = t
    def getDiscovered(self):
        return self.discovered

    def setFinished(self, t):
        self.finished = t
    def getFinished(self):
        return self.finished

    def setColor(self, c):
        self.color = c
    def getColor(self):
        return self.color

    def setPred(self, p):
        self.predecessor = p
    def getPred(self, p):
        return self.predecessor

    # adds a Vertex object to connectedTo.
    # ! remember, the keys in connectedTo are Vertex objects, not strings.

    def addNeighbor(self, nbr, weight=0): # nbr is a Vertex object
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


        # additional properties for scc:
        self.time = 0


        # Items will be added to this list as they are finished in dfs
        self.topSorted = []


    # Accepts a string and creates a Vertex object in vertList corresponding to the given key
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices = self.numVertices + 1
        return newVertex

    # Accepts a string and returns a Vertex object if one exists
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList


    # _from and _to are strings, if these keys do not exist in the vertList Dictionary,
    # this function creates the corresponding Vertex objects if needed.
    # 
    # the addNeighbor method is then called on _from to create an edge between the desired nodes
    def addEdge(self, _from, _to, cost=0):
        if _from not in self.vertList.keys():
            nv = self.addVertex(_from)
        if _to not in self.vertList.keys():
            nv = self.addVertex(_to)

        self.vertList[_from].addNeighbor(self.vertList[_to], weight=0)

    # returns a list of keys for the verList dictionary (strings)
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    # additional Graph methods:
    def tick(self):
        self.time = self.time + 1

    def getTime(self):
        return self.time


    # The next two methods implement dfs:
    def dfs(self):

        for aVertex in self:
            # provide initial values for graph items, 
            # this may not be necessary given the way I have defined the instance variables
            aVertex.setColor('white')
            aVertex.setPred(-1)
            
            

        for aVertex in self:
            # initially these are all white, but that may change as .visit() is called on each element
            if aVertex.getColor() == 'white':
                self.visit(aVertex)


    def visit(self, start):
        
        # increment time and mark as discovered:
        self.tick()
        start.setDiscovered(self.getTime())
        start.setColor('gray')

        for nextVertex in start.getConnections():

            # recursively visit undiscovered nodes
            if nextVertex.getColor() == 'white':

                nextVertex.setPred(start)
                self.visit(nextVertex)
        # at this point the stack of recursive calls of .visit() has returned and this vertex has been
        # completely explored, now we can mark a finish time and set this color to black.

        self.tick()
        start.setFinished(self.getTime())
        start.setColor('black')

        # since at this point we have easy access to this vertex.  It will be inserted in the list of 
        # topologically sorted vertices.
        # 
        # items inserted at the beginning of the list so that the front of the list will be the last item finished.
        self.topSorted.insert(0,start.getId())





    def build(self, _list):
        # _list --> [key, [connections, ...], ...]
        
        for i in range(len(_list)):
            element = _list[i]
            key = element[0]
            connections = element[1]

            for j in range(len(connections)):
                connection = connections[j]

                self.addEdge(key, connection)


    def transpose(self):

        newGraph = Graph()

        for vertex in self:
            _to = vertex.getId()

            for connection in vertex.getConnections():
                _from = connection.getId()

                newGraph.addEdge(_from, _to)

        return newGraph

    def getSCC(self, topSortedList):

        sccVals = []
        
        for aVertex in self:
            aVertex.setColor('white')


        for  _id in topSortedList:

            currentVertex = self.getVertex(_id)


            if currentVertex.getColor() == 'white':
                componentsList = []
                # pass componentsList and avertex to sccVisit to fill the list
                sccVals.append(self.sccVisit(currentVertex, componentsList))
            #print "continuing to next vertex"
            #print sccVals

        return sccVals
    
    def sccVisit(self, start, vals):

        # mark start as discovered
        start.setColor('black')

        #add its Name to the list of connections:
        vals.append(start.getId())


        for aVertex in start.getConnections():
            # if this vertex is undiscovered
            if aVertex.getColor() == 'white':
                
                # recursively visit each other node, further appending the list with any nodes that were visited.
                self.sccVisit(aVertex, vals)

        # return the list containing everything visited
        return vals

                


        


elements = [

  ['V0', ['V2', 'V3']],
  ['V1', ['V0', 'V2']],
  ['V2', ['V0', 'V4', 'V5']],
  ['V3', ['V5', 'V7']],
  ['V4', []],
  ['V5', ['V3', 'V6', 'V7']],
  ['V6', ['V4', 'V5']],
  ['V7', ['V5', 'V6']],
]





# TESTING: _____________________



def printGraph(g):
    for vertex in g:
        print vertex

g = Graph()
g.build(elements)
g.dfs()

ng = g.transpose()

print "\nGraph:"
printGraph(g)
print "\nTransposed Graph:"
printGraph(ng)

# view discovered and finished times:
print "\nDiscovered / FInished:"
for vertex in g:
    print ( vertex.getId() +  ": " + str(vertex.getDiscovered()) +  ' / ' + str(vertex.getFinished()) )

# topological sort:
order =  g.topSorted

print "\nTopologial Sort:"
print order





print "\nStrongly connected components:"
print ng.getSCC(order)





















