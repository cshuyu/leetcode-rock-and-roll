// Last updated: 2/23/2026, 6:46:31 PM
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
    public TreeNode convertBST(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        inOrder(list, root);
        
        int[] greater = new int[list.size()];
        int count = 0;
        
        for(int i = list.size() - 1; i >= 0; i--){
            count += list.get(i);
            greater[i] = count;
        }
        
        int arrayIndex = 0;
        TreeNode index = root;
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        while(true){
            while(index != null){
                stack.push(index);
                index = index.left;
            }
            
            if(stack.isEmpty() == false){
                TreeNode curr = stack.pop();
                curr.val = greater[arrayIndex];
                arrayIndex++;
                
                if(curr.right != null){
                    index = curr.right;
                }
            }
            else{
                break;
            }
        }
        
        return root;
        
    }
    
    
    private void inOrder(ArrayList<Integer> ret, TreeNode root){
        if(root == null) return;
        
        inOrder(ret, root.left);
        ret.add(root.val);
        inOrder(ret, root.right);
    }
}