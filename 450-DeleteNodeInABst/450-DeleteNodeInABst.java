// Last updated: 2/23/2026, 6:47:17 PM
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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null)
            return null;
        if(key>root.val)
            root.right = deleteNode(root.right, key);
        else if(key<root.val)
            root.left = deleteNode(root.left, key);
        else {
            if(root.left==null && root.right==null) {
                root=null;
            }
            else if(root.right!=null){
                root.val = after(root);
                root.right = deleteNode(root.right, root.val);
            }
            else{
                root.val = pre(root);
                root.left = deleteNode(root.left, root.val);
            }         
        }
        return root;
    }
    
    private int after(TreeNode root) {
        root = root.right;
        while(root.left!=null) {
            root = root.left;     
        } 
        return root.val;
    }
    
    private int pre(TreeNode root) {
        root = root.left;
        while(root.right!= null) {
            root = root.right;
        }
        System.out.print(root.val);
        return root.val;
    }
}