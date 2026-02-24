// Last updated: 2/23/2026, 6:47:02 PM
public class Solution {
    public String encode(String s) {
        if(s == null || s.length() == 0) return s;
        int size = s.length();
        
        String[][] dp = new String[size][size];
        
        for(int l = 0; l < size; l++){
            for(int i = 0; i < size - l; i++){
                int j = i + l;
                String curr = s.substring(i, i + l + 1);
                
                if(l < 4){
                    dp[i][j] = curr;
                }
                else{
                    dp[i][j] = curr;
                    for(int k = i; k < j; k++){
                        if((dp[i][k] + dp[k + 1][j]).length() < dp[i][j].length()){
                            dp[i][j] = dp[i][k] + dp[k + 1][j];
                        }
                    }
                }
                
                //handle the curr
                
                for(int k = 0; k < curr.length(); k++){
                    String repeated = curr.substring(0, k + 1);
                    
                    if(repeated != null && curr.length() % repeated.length() == 0 && curr.replace(repeated, "").length() == 0){
                        String encode = curr.length() / repeated.length() + "[" + dp[i][i+k] + "]";
                        if(encode.length() < dp[i][j].length()){
                            dp[i][j] = encode;
                        }
                    }
                }
                
            }
        }
        
        return dp[0][size - 1];
    }
}