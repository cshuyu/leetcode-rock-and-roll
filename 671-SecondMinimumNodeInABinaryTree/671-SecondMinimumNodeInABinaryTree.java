// Last updated: 2/23/2026, 6:46:08 PM
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
    public int findSecondMinimumValue(TreeNode root) {
        if(root==null) {
           return -1; 
        }
        long val = helper(root);
        if(val==Long.MAX_VALUE)
            return -1;
        else
            return (int)val;
    }
    
    private long helper(TreeNode node) {
        long min = Long.MAX_VALUE;
        if(node.left==null && node.right==null)
            return min;
        if(node.left.val == node.val && node.right.val == node.val) {
            return Math.min(helper(node.left), helper(node.right));
        }
        if(node.left.val == node.val) {
            return Math.min(helper(node.left), node.right.val);
        }
        if(node.right.val == node.val) {
            return Math.min(helper(node.right), node.left.val);
        }
        return min;
    }
    
}