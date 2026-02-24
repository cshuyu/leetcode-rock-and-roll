// Last updated: 2/23/2026, 6:46:47 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int max = 0;
    private int count = 1;
    private Integer prev = null;
    
    public int[] findMode(TreeNode root) {
        if(root == null) return new int[0];
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        helper(root, list);
        
        int[] ret = new int[list.size()];
        
        for(int i = 0; i < list.size(); i++){
            ret[i] = list.get(i);
        }
        
        return ret;
    }
    
    private void helper(TreeNode root, ArrayList<Integer> list){
        if(root == null) return;
        
        helper(root.left, list);
        if (prev != null) {
            if (root.val == prev)
                count++;
            else
                count = 1;
        }
        
        if(count > max){
            max = count;
            list.clear();
            list.add(root.val);
        }
        else if(count == max){
            list.add(root.val);
        }
        
        prev = root.val;
        helper(root.right, list);
    }
}