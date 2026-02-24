// Last updated: 2/23/2026, 6:44:43 PM
class Solution {
    public int maxNumberOfBalloons(String text) {
        String pattern = "balloon";
        return helper(text, pattern);
    }
    
    private int helper(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[] textFreq = new int[26];
        int[] patternFreq = new int[26];
        
        for(int i=0; i<n; i++) {
            textFreq[text.charAt(i)-'a']++;
        }
        for(int j=0; j<m; j++) {
            patternFreq[pattern.charAt(j)-'a']++;
        }
        
        int res = Integer.MAX_VALUE;
        for(int k=0; k<26; k++) {
            if(patternFreq[k]>0)
                res = Math.min(res, textFreq[k]/patternFreq[k]);
        }
        return res;
    }
}