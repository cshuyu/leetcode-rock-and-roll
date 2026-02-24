// Last updated: 2/23/2026, 6:46:10 PM
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
    public boolean findTarget(TreeNode root, int k) {
        if(root==null && k!=0)
            return false;
        List<Integer> lst = new ArrayList<>();
        inOrder(root, lst);
        int i = 0;
        int j = lst.size()-1;
        while(i<j) {
            if(lst.get(i)+lst.get(j)==k) {
                return true;
            }
            else if(lst.get(i)+lst.get(j)<k) {
                i++;
            }
            else {
                j--;
            }
        }
        return false;
    }
    
    private void inOrder(TreeNode node, List<Integer> lst) {
        if(node==null)
            return;
        inOrder(node.left, lst);
        lst.add(node.val);
        inOrder(node.right, lst);
    }
}