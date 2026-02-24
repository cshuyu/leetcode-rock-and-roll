// Last updated: 2/23/2026, 6:46:36 PM
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
    public int getMinimumDifference(TreeNode root) {
        int min = Integer.MAX_VALUE;
        int prev = -1;
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        TreeNode index = root;
        
        while(true){
            while(index != null){
                stack.push(index);
                index = index.left;
            }
            
            if(!stack.isEmpty()){
                TreeNode top = stack.pop();
                if(prev == -1){
                    prev = top.val;
                }
                else{
                    int diff = top.val - prev;
                    min = Math.min(min, diff);
                    prev = top.val;
                }
                index = top.right;
            }
            else{
                break;
            }
        }
        
        return min;
        
    }
}