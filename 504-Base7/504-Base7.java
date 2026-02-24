// Last updated: 2/23/2026, 6:46:45 PM
public class Solution {
    public String convertToBase7(int num) {
        boolean negative = false;
        
        if(num < 0){
          num = num * -1;
          negative = true;
        }
        
        Stack<Integer> stack = new Stack<Integer>();
        
        while(num >= 7){
            stack.push(num % 7);
            num = num / 7;
        }
        
        StringBuilder sb = new StringBuilder();
        if(negative){
            sb.append("-");
        }
        
        sb.append(num);
        
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        
        return sb.toString();
        
    }
}