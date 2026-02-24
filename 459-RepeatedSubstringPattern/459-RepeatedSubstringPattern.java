// Last updated: 2/23/2026, 6:47:07 PM
public class Solution {
    public boolean repeatedSubstringPattern(String s) {
        if(s == null || s.length() <= 1) return false;
        
        int size = s.length();
        
        for(int i = size / 2; i > 0; i--){
            if(size % i == 0){
                String pre = s.substring(0, i);
                String post = s.substring(i);
                String reappend = post + pre;
                if(reappend.equals(s)){
                    return true;
                } 
            }
        }
        
        return false;
    }
}