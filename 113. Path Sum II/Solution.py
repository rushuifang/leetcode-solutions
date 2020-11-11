# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(node, curr_path, target):
            if not node:
                return
            if node.val == target and not node.left and not node.right:
                res.append(curr_path + [node.val])
                return
            dfs(node.left, curr_path + [node.val], target - node.val)
            dfs(node.right, curr_path + [node.val], target - node.val)

        dfs(root, [], sum)
        return res
