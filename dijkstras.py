class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # {key = Vertex object : value = int}
        self.distance = 0
        self.pred = None

    # adds a Vertex object to connectedTo.
    # ! remember, the keys in connectedTo are Vertex objects, not strings.
    def setPred(self, nbr):
        self.pred = nbr

    def getPred(self):
        return self.pred

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

    def getDistance(self):
        return self.distance

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

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

        self.vertList[_from].addNeighbor(self.vertList[_to], cost)

    # returns a list of keys for the verList dictionary (strings)
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




def buildGraph(connectionList):

    graph = Graph()

    for connection in connectionList:
        _from = connection[0]
        _to = connection[1]
        weight = connection[2]

        graph.addEdge(_from, _to, weight)

    return graph

connections = [
    ['a', 'b', 4],
    ['a', 'c', 2],
    ['c', 'a', 2],
    ['c', 'b', 1],
    ['c', 'd', 8],
    ['c', 'e', 10],
    ['b', 'c', 1],
    ['b', 'd', 5],
    ['d', 'c', 8],
    ['d', 'e', 2],
    ['d', 'z', 6],
    ['e', 'c', 10],
    ['e', 'd', 2],
    ['e', 'z', 3],
    ['z', 'e', 3],
    ['z', 'd', 6]
]

g = buildGraph(connections)



def getSmallest(_list):

    smallestIndex = 0

    for i in range(len(_list)):
        if (_list[i].getDistance() < _list[smallestIndex].getDistance()):
            smallestIndex = i

    return _list.pop(smallestIndex)


"""
a = Vertex('a')
a.distance = 10
b = Vertex('b')
b.distance = 5
c = Vertex('c')
c.distance = 20


l = [c,b,a]
print l

print getSmallest(l).getId()
print l

print getSmallest(l).getId()
print l

print getSmallest(l).getId()
print l

"""

# Note: "infinity" for this algorithm is 1000
def dijkstra(graph, start):

    # first set all the distances of the graph to infinity (for this implementation, 1000 will work)
    for vertex in graph:
        vertex.distance = 1000

    # set start distance to 0
    graph.getVertex(start).distance = 0

    path = []

    # Remember: 
    # start = current vertex
    # each nbr is each vertex we are traveling to from start
    path.append(graph.getVertex(start))

    # execute dijkstras algorithm until there are no verteces left to explore.
    while len(path) > 0:

        curr = getSmallest(path)

        for nbr in curr.getConnections():

            currentDistance = curr.getDistance() + curr.getWeight(nbr)

            # if the weight to get to nbr is less than the distance of nbr, then reset nbr.distance to the new, smaller value.

            if currentDistance < nbr.getDistance():
                # set predecessor before editing the distance, and adding it to the priority queue
                nbr.setPred(curr)

                nbr.distance = currentDistance

                path.append(nbr)


dijkstra(g, 'a')


v = g.getVertex('z')

while v != None:
    print v.getId()
    v = v.getPred()

































        
