# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        s = []

        def printNode(node):
            if node:
                s.append(node.val)
                if node.left is not None:
                    printNode(node.left)
                if node.right is not None:
                    printNode(node.right)

        printNode(root)
        return "#".join(map(str, s))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            # corner case handle for empty tree
            return None
        node_values = deque(int(value) for value in data.split("#"))

        def helper(lower_bound, upper_bound):

            if node_values and lower_bound < node_values[0] < upper_bound:

                root_value = node_values.popleft()
                root_node = TreeNode(root_value)

                root_node.left = helper(lower_bound, root_value)
                root_node.right = helper(root_value, upper_bound)

                return root_node

        # ---------------------------------------------

        return helper(float("-inf"), float("inf"))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans