// Last updated: 2/23/2026, 6:46:46 PM
public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] ret = new int[nums.length];
        
        Arrays.fill(ret, - 1);
        
        Stack<Integer> stack = new Stack<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();  //index => greater
        
        int size = nums.length;
        
        for(int i = 0; i < size * 2; i++){
            int realIndex = i % size;
            int n = nums[realIndex];
            
            if(stack.isEmpty() || nums[stack.peek() % size] >= n){
                stack.push(i);
            }
            else{
                if(n > nums[stack.peek() % size]){
                    while(!stack.isEmpty() && nums[stack.peek() % size] < n){
                        int index = stack.pop();
                        if(index < size){
                            ret[index] = n;
                        }
                    }
                    
                    stack.push(i);
                }
            }
        }
        
        return ret;
    }
}