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
    public int maxDepth(TreeNode root) {
        return depth(root, 0);
    }
    private int depth(TreeNode node, int n){
        if(node == null) return n;
        int t = n;
        return Math.max(depth(node.left, n+1), depth(node.right, n+1));
    }
}