// Last updated: 2/23/2026, 6:45:11 PM
class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        return findPattern(s+s, goal);
    }
    
    /** Build  the longest proper prefix & suffix array.
        
        lps[i] is for the substring of pattern[0:i], the
        longest *proper* prefix which is also a suffix.
        For example, 
          pattern = "abcabd", lps[4] is to find the longest
          prefix which is also a suffix for substring of
          "abcab". The size is 2, because the prefix "ab" is 
          also a suffix of the substring.
         
          Another example = "aaaab", lps[3] is to find the 
          longest length from substring "aaaa". The size is 3
          because 1. we entire string ("aaaa") is not a proper
          prefix. 2. proper fix "aaa" is also a suffix of the string.
          so the size is 3.
      */
    int[] buildLongestPrefixSuffix(String pattern) {
        if (pattern.length() == 0) return new int[0];
        int[] lps = new int[pattern.length()]; 
        
        // No proper prefix for a sigle char, so it's lps is 0.
        lps[0] = 0;
        
        // for pattern[0:i]
        int i = 1;
        int prevLen = lps[i-1];
        while(i<pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(prevLen)) {
                lps[i] = prevLen + 1;
                prevLen++;
                i++;
            } else {
                // Find shorter prefix that equals to suffix of
                // substring pattern[0:i-1].
                if (prevLen == 0) {
                    // Means that pattern[0] != pattern[i] and no prefix same
                    // as the suffix of pattern[0:i-1]
                    lps[i] = 0;
                    i++;
                } else {
                    // Continue to find a shorter prefix that same as the suffix
                    // of pattern[0:i-1]
                    prevLen = lps[prevLen -1];
                }
            }
            
        }
        
        return lps;
    }
    
    /** Find the pattern from the text. */
    private boolean findPattern(String text, String pattern) {
        if (pattern.isEmpty()) return true;
        if (pattern.length() > text.length()) return false;
        
        // lps[i] is the longest length for string pattern[0:i] that
        // exists a prefix which is also a suffix.
        int[] lps = buildLongestPrefixSuffix(pattern);
        
        int textIdx = 0, patIdx = 0;
        while(textIdx<text.length() && patIdx < pattern.length()) {
            if (text.charAt(textIdx) == pattern.charAt(patIdx)) {
                textIdx++;
                patIdx++;
            } else {
                // Now we know that 
                // 1. text[0:textIdx-1] == pattern[;:patIdx-1]
                // 2. text[textIdx] != pattern[patIdx]
                // We need to decide which char from pattern to compare 
                // against text[textIdx]. Note that no need to compare
                // against any chars from text[0:textIdx-1].
                if (patIdx == 0) {
                    // If this is the first char in the pattern, move 
                    // the text char to right by one.
                    textIdx++;
                } else {
                    // Otherwise, checking lps table to see how many chars
                    // to move for pattern.
                    patIdx = lps[patIdx-1];   
                }
            }
        }
        if (patIdx == pattern.length()) return true;
        return false;
        
    }
}