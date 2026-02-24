// Last updated: 2/23/2026, 6:46:58 PM
public class Solution {
    public int magicalString(int n) {
        if(n < 1) return 0;
        
        StringBuilder magic = new StringBuilder("122");
        
        if(n <= 3) return 1;
        
        int tail = 2;
        int indicator = 2;
        
        int count = 0;
        
        while(magic.length() < n){
            if(magic.charAt(indicator) == '1'){
               if(magic.charAt(tail) == '2'){
                    magic.append("1");
                }
                else{
                    magic.append("2");
                }
                tail += 1;
                indicator += 1;
            }
            else{
                if(magic.charAt(tail) == '2'){
                    magic.append("11");
                }
                else{
                    magic.append("22");
                }
                tail += 2;
                indicator++;
            }
        }
        
        for(int i = 0; i < n; i++){
            if(magic.charAt(i) == '1'){
                count++;
            }
        }
        
        return count;
    }
}