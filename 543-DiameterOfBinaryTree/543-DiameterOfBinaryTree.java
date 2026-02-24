// Last updated: 2/23/2026, 6:46:29 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int max=0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return max;
    }
    
    public int maxDepth(TreeNode node) {
        if(node==null)
            return 0;
        int left = maxDepth(node.left);
        int right = maxDepth(node.right);
        max = Math.max(left+right, max);
        return 1+Math.max(left, right);
    }
}