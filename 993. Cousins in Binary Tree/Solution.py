# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = []
        queue.append((root, None, 0))
        res = []

        while queue:
            node, parent, depth = queue.pop(0)
            if len(res) == 2:
                break
            if node.val == x or node.val == y:
                res.append((parent, depth))
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        return res[0][0] != res[1][0] and res[0][1] == res[1][1]


# dfs
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		# store (parent, depth) tuple
		res = [] 
        
		# dfs
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)

		# unpack two nodes found
        node_x, node_y = res  
		
		# compare and decide whether two nodes are cousins
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]