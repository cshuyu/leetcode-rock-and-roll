// Last updated: 2/23/2026, 6:47:09 PM
public class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Interval> stack = new Stack<Interval>();
        
        
        for(int num : nums){
            if(stack.isEmpty() || stack.peek().min > num){
                stack.push(new Interval(num, num));
            }
            else if(stack.peek().min < num){
                Interval top = stack.pop();
                
                if(num < top.max){
                    return true;
                }
                else{
                    top.max = num;
                    
                    while(!stack.isEmpty() && stack.peek().max <= top.max){
                        stack.pop();
                    }
                    
                    if(!stack.isEmpty() && stack.peek().min < num) return true;
                    
                    stack.push(top);
                }
                
                
            }
        }
        
        return false;
        
        
    }
    
    class Interval{
        int min;
        int max;
        
        public Interval(int min, int max){
            this.min = min;
            this.max = max;
        }
    }
}