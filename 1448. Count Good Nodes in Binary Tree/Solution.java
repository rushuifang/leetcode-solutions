/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res;
    public int goodNodes(TreeNode root) {
        goodNodesHelper(root, Integer.MIN_VALUE);
        return res;
    }
    
    public void goodNodesHelper(TreeNode root, int max) {
        if (root == null) return;
        if (root.val >= max) {
            res++;
            max = root.val;
        }
        goodNodesHelper(root.left, max);
        goodNodesHelper(root.right, max);
    }
}