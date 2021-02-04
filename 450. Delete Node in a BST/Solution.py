# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMin(self, node):
        while node.left:
            node = node.left
        return node
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                minNode = self.getMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, root.val)
                
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root