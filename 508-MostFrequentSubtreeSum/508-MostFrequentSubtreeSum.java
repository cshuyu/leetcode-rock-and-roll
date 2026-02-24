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
    public int[] findFrequentTreeSum(TreeNode root) {
        if(root == null) return new int[0];
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        helper(root, map);
        
        int max = Integer.MIN_VALUE;
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for(Integer key: map.keySet()){
            if(map.get(key) > max){
                list.clear();
                list.add(key);
                max = map.get(key);
            }
            else if(map.get(key) == max){
                list.add(key);
            }
            else{
                continue;
            }
        }
        
        int[] ret = new int[list.size()];
        
        for(int i = 0; i < list.size(); i++){
            ret[i] = list.get(i);
        }
        
        return ret;
        
        
    }
    
    private int helper(TreeNode root, HashMap<Integer, Integer> map){
        if(root.left == null && root.right == null){
          countFrequency(map, root.val);
           return root.val; 
        } 

        if(root.left == null && root.right != null){
            int right = helper(root.right, map);
        
            int sum = right + root.val;
            countFrequency(map, sum);
            
            return sum;
        }
        else if(root.left != null && root.right == null){
            int left = helper(root.left, map);
    
            int sum = left  + root.val;
            countFrequency(map, sum);
        
            return sum;
        }
        else{
           int left = helper(root.left, map);
        
            int right = helper(root.right, map);
        
            int sum = left + right + root.val;
            countFrequency(map, sum);
        
            return sum; 
        }
    }
    
    private void countFrequency(HashMap<Integer, Integer> map, int sum){
        if(map.containsKey(sum)){
            map.put(sum, map.get(sum) + 1);
        }
        else{
            map.put(sum, 1);
        }
    }
}