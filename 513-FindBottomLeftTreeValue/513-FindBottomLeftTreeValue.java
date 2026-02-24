// Last updated: 2/23/2026, 6:46:42 PM
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
    public int findBottomLeftValue(TreeNode root) {
        int ret = root.val;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        int index = 0;
        queue.add(root);
        int size = queue.size();
        
        while(!queue.isEmpty()){
            TreeNode curr = queue.remove();
            if(curr.left != null){
                queue.add(curr.left);
            }
            if(curr.right != null){
                queue.add(curr.right);
            }
            
            if(index == 0) ret = curr.val;
            index++;
            
            if(index == size){
                index = 0;
                size = queue.size();
            }
        }
        
        return ret;
        
    }
}