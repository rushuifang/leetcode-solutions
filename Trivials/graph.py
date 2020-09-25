class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        else:
            self.gdict = gdict

    def getKeys(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findEdges()

    def findEdges(self):
        edgeName = []
        for vertex in self.gdict:
            for edges in self.gdict[vertex]:
                if {vertex, edges} not in edgeName:
                    edgeName.append({vertex, edges})
        return edgeName

    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = ""

    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = vertex2


graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"],
}

g = graph(graph_elements)
# print(g.getKeys())

# print(g.edges())

# g.addVertex("f")
# print(g.getKeys())

# g.addEdge({"a", "e"})
# g.addEdge({"a", "c"})
print(g.edges())