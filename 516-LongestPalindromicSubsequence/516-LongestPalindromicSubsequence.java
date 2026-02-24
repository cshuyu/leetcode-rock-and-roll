// Last updated: 2/23/2026, 6:46:41 PM
class Solution {
    public int longestPalindromeSubseq(String s) {
        int length = s.length();
        int[][] longestPalindromeArray = new int[length][length];
        for(int i=length-1; i>=0; i--) {
            for(int j=i; j<length; j++) {
                if(i==j)
                    longestPalindromeArray[i][j] = 1;
                else if(i+1==j) {
                    if(s.charAt(i)==s.charAt(j))
                        longestPalindromeArray[i][j] = 2;
                    else
                        longestPalindromeArray[i][j] = 1;
                }
                else if(s.charAt(i)==s.charAt(j)) {
                    longestPalindromeArray[i][j] = longestPalindromeArray[i+1][j-1]+2;
                }
                else{
                    longestPalindromeArray[i][j] = Math.max(longestPalindromeArray[i+1][j], longestPalindromeArray[i][j-1]);
                }
            } 
        }
        return longestPalindromeArray[0][length-1];
    }
}