// Last updated: 2/23/2026, 6:46:39 PM
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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ret = new ArrayList<Integer>();
        
        if(root == null) return ret;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.add(root);
        int count = 0;
        int size = queue.size();
        int max = Integer.MIN_VALUE;
        
        while(!queue.isEmpty()){
            TreeNode curr = queue.remove();
            max = Math.max(max, curr.val);
            if(curr.left != null){
                queue.add(curr.left);
            }
            if(curr.right != null){
                queue.add(curr.right);
            }
            count++;
            
            if(count == size){
                count = 0;
                size = queue.size();
                ret.add(max);
                max = Integer.MIN_VALUE;
            }
        }
        
        return ret;
    }
}