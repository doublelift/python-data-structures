# Implementation of a graph using an adjacency list:

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}  # {key = Vertex object : value = int}

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

		self.vertList[_from].addNeighbor(self.vertList[_to], weight)

    # returns a list of keys for the verList dictionary (strings)
	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

		



























