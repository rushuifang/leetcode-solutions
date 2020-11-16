"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        def helper(node):
            scanner = node.next
            while scanner:
                if scanner.left:
                    scanner = scanner.left
                    break
                if scanner.right:
                    scanner = scanner.right
                    break
                scanner = scanner.next

            if node.right:
                node.right.next = scanner
            if node.left:
                node.left.next = node.right if node.right else scanner

            if node.right:
                helper(node.right)
            if node.left:
                helper(node.left)
            return node

        if not root:
            return None
        return helper(root)