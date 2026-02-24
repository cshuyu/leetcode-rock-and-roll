// Last updated: 2/23/2026, 6:44:46 PM
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if(text1==null || text2==null || text1.length()==0 || text2.length()==0)
            return 0;
        
        int text1_size = text1.length();
        int text2_size = text2.length();
        
        int[][] tmp = new int[text1_size+1][text2_size+1];
        for (int i=0; i<text1_size+1; i++) {
              tmp[i][0] = 0;
        }
        for(int j=0; j<text2_size+1; j++) {
            tmp[0][j] =0;
        }
        
        if(text1.charAt(0)==text2.charAt(0))
            tmp[1][1] = 1;
        else
            tmp[1][1] = 0;
        
        for(int i=1; i<text1_size+1; i++) {
            for(int j=1; j<text2_size+1; j++) {
                if(text1.charAt(i-1) == text2.charAt(j-1))
                    tmp[i][j] = tmp[i-1][j-1]+1;
                else
                    tmp[i][j] = Math.max(tmp[i-1][j], tmp[i][j-1]);
            }            
        }
        
        return tmp[text1_size][text2_size];
    }
}