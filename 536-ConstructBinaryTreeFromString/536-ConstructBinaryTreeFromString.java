// Last updated: 2/23/2026, 6:46:32 PM
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
    public TreeNode str2tree(String s) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        int index = 0;
        
        while(index < s.length()){
            char ch = s.charAt(index);
            
            if((ch >= '0' && ch <= '9') || ch == '-'){
                int start = index;
                index++;
                while(index < s.length() && s.charAt(index) >= '0' && s.charAt(index) <= '9'){
                    index++;
                }
                
                int value = Integer.valueOf(s.substring(start, index));
                TreeNode curr = new TreeNode(value);
                
                
                if(stack.isEmpty() == false){
                    TreeNode parent = stack.peek();
                    if(parent.left != null){
                        parent.right = curr;
                    }
                    else{
                        parent.left = curr;
                    }
                }
                
                stack.push(curr);
            }
            else if(ch == ')'){
                stack.pop();
                index++;
            }
            else{
                index++;
            }
        }
        if(stack.isEmpty()) return null;
        
        return stack.peek();
    }
    
}