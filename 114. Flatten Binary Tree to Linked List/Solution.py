# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        nodes = []

        while stack:
            node = stack.pop()
            if node:
                nodes.append(node)
                stack.append(node.right)
                stack.append(node.left)

        root = nodes.pop(0)
        for node in nodes:
            root.right = node
            root.left = None
            root = root.right
            
# Even though root is correct, but this won't do
        # root = None
        # while nodes:
        #     root = TreeNode(nodes.pop().val, None, root)
        # print(root)