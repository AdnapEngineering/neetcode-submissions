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
        // depth = 1 + max(left_depth, right_depth)
        // Base case:
        if ( root == null) return 0;

        // We need recursive post order dfs. 
        int leftDepth = maxDepth(root.left);

        int rightDepth = maxDepth(root.right);

        return 1 + Math.max(leftDepth, rightDepth);

    }
}
