"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# My solution
class Solution:
    def maxDepth(self, root: "Node") -> int:
        res = 1
        if not root:
            return 0
        for child in root.children:
            res = max(res, self.maxDepth(child) + 1)
        return res


# BFS solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        queue.append((root, 1))
        visited = set()
        max_depth = 0
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            for child in node.children:
                if child not in visited:
                    queue.append((child, depth + 1))
                    visited.add(child)

        return max_depth


# DFS solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        visited = set()
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            for child in node.children:
                if child not in visited:
                    visited.add(child)
                    stack.append((child, depth + 1))
        return max_depth