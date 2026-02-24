// Last updated: 2/23/2026, 6:44:28 PM
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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode tmp = helper(root, p, q);
        if(tmp==null)
            return null;
        else if(tmp==p)
            return helper(p, q, q) != null ? p : null;
        else if(tmp==q)
            return helper(q, p, p) != null ? q : null;
        else
            return tmp;
    }
    
    /** 
     * Returns 1) TreeNode p or 2) TreeNode q or 3) their LCA or null if none is found.
     *   - TreeNode p or q: the other node might or might not exist in its subtree, but not vice versa.
     */
    private TreeNode helper(TreeNode node, TreeNode p, TreeNode q) {
        if(node==null || node==p || node==q) {
            return node;
        }
        TreeNode left = helper(node.left, p, q);
        TreeNode right = helper(node.right, p, q);
        if(left!=null && right!=null)
            return node;
        else if(left==null && right==null)
            return null;
        else if(left==null)
            return right;
        else
            return left;
    }
}