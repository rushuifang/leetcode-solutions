# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        if not root.left and not root.right:
            return depth
        elif not root.right:
            depth += self.minDepth(root.left)
            return depth
        elif not root.left:
            depth += self.minDepth(root.right)
            return depth
        else:
            depth += min(self.minDepth(root.left), self.minDepth(root.right))
            return depth