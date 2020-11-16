# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            if node.left:
                node.left.val += node.val*10
            if node.right:
                node.right.val += node.val*10
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root)