# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1: return root
        
        L = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:L], postorder[:L])
        root.right = self.buildTree(inorder[L+1:], postorder[L:-1])
        return root