# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                firstNode = queue.pop(0)
                level.append(firstNode.val)
                if firstNode.left:
                    queue.append(firstNode.left)
                if firstNode.right:
                    queue.append(firstNode.right)
            res.append(level)
        return res
