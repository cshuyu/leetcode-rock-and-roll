// Last updated: 2/23/2026, 6:46:49 PM
public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        Stack<Integer> stack = new Stack<Integer>();
        
        for(int n: nums){
            if(stack.isEmpty() || stack.peek() >= n){
                stack.push(n);
            }
            else{
               while(!stack.isEmpty() && stack.peek() < n){
                   map.put(stack.pop(), n);
               }
               
               stack.push(n);
            }
        }
        
        int[] ret = new int[findNums.length];
        
        for(int i = 0; i < findNums.length; i++){
            int num = findNums[i];
            if(map.containsKey(num)){
                ret[i] = map.get(num);
            }
            else{
                ret[i] = -1;
            }
        }
        
        return ret;
    }
}