# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        if not root.left and not root.right:
            return depth
        if not root.left and root.right:
            depth += self.maxDepth(root.right)
            return depth
        if not root.right and root.left:
            depth += self.maxDepth(root.left)
            return depth
        depth += max(self.maxDepth(root.right), self.maxDepth(root.left))
        return depth