class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {} # {key = Vertex object : weight}
    self.visited = False

  def addNeighbor(self, nbr, weight=0): # nbr is a Vertex object
    self.connectedTo[nbr] = weight

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # returns a list of vertex objects
  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, nbr):  # nbr is a Vertex Object
    return self.connectedTo[nbr]

class Graph:
  def __init__(self):
    self.vertList = {} # {key = vertex name: value = Vertex object}
    self.numVertices = 0

  def addVertex(self, key): # key is a string, this function creates a vertex object from the string and adds it to 
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    self.numVertices = self.numVertices + 1
    return newVertex

  def getVertex(self, name):
    if name in self.vertList:
      return self.vertList[name]
    else:
      return None

  def addEdge(self, _from, _to, cost=0):
    if _from not in self.vertList:
      nv = self.addVertex(_from)
    if _to not in self.vertList:
      nv = self.addVertex(_to)

    self.vertList[_from].addNeighbor(self.vertList[_to], cost)

    # returns all the keys in the vertList
  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())


# buildBoard returns a graph representing a chessboard with sideLength: n

def convertToId(x,y,n):
  return (x + (n * y))


def getLegalMoves(x, y, n):

  possibleMoves = [
      [x + 1, y + 2],
      [x + 2, y + 1],
      [x + 2, y - 1],
      [x + 1, y - 2],
      [x - 1, y - 2],
      [x - 2, y - 1],
      [x - 2, y + 1],
      [x - 1, y + 2]
    ]

  legalMoves = []

  for pm in possibleMoves:
    sideLength = range(n)

    if (pm[0] in sideLength) and (pm[1] in sideLength):
      lm = convertToId(pm[0], pm[1], n)
      legalMoves.append(lm)

  return legalMoves



def buildBoard(n):

  graph = Graph()

  for x in range(n):
    for y in range(n):

      square = convertToId(x,y,n)

      legalMoves = getLegalMoves(x,y,n)

      for lm in legalMoves:

        graph.addEdge(square, lm)

  return graph

"""

cBoard = buildBoard(5)

for vertex in cBoard:
  print vertex

"""
#add a visited attribute to the vertex class.
def knightsTour(start, board, depth, visited):

  # there are three trivial cases in this function:
  #  1) enough squares have been visited (return True)
  #  2) start has already been visited, (return False)
  #  3) all the edges of a square have been visited and none were successful traversals (return False)
  
  # trivial case 1:  
  if (len(visited) >= depth):
    #print visited
    return visited

  # trivial case 2: 
  if start.visited:
    return False

  # mark start as visited before recursing into its connections.
  start.visited = True
  # add it to the list of visited squares:
  visited.append(start)

  # recursively visit each one of starts edges while each one does not result in a success.
  result = False

  for edge in start.getConnections():
    result = knightsTour(edge, board, depth, visited)
    
    # if the knghts tour was successful, return the list, stopping the for loop
    if result:
      return visited

  # if the function has reached this point then no connection of start has resulted in a success
  # therefore we need to backtrack.

  # remove start from the list
  visited.pop()
  # unmark start so it can be visited in later recursive calls.
  start.visited = False

  # Finally return false to so the previous call in the stack knows this call was a dud.
  return False

  

cBoard = buildBoard(5)

start = cBoard.getVertex(0)

touredSquares = knightsTour(start, cBoard, 25, [])


l = []
for sq in touredSquares:
  l.append(sq.getId())
print l


























































