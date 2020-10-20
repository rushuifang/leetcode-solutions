"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]

        newNode = Node(node.val)
        self.visited[node] = newNode
        newNode.neighbors = []

        for child in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(child))
        return newNode