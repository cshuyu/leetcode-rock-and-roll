# Last updated: 2/23/2026, 6:46:43 PM
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # d[i, j] is the LPS of string s[i:j+1].
        # Rule:
        # if s[i] == s[j]: d[i,j] = d[i+1,j-1] + 1
        # else d[i,j] = max(d[i+1, j], d[i,j-1])
        if len(s) <= 1:
            return len(s)
        
        d = [[1 for _ in range(len(s))] for __ in range(len(s))]
        for i in range(len(s) -1):
            if s[i] == s[i+1]:
                d[i][i+1] = 2
        
        for w in range(2, len(s)):
            for i in range(len(s) - w):
                j = i + w
                if s[i] == s[j]:
                    d[i][j] = d[i+1][j-1] + 2
                else:
                    d[i][j] = max(d[i+1][j], d[i][j-1])
               
        return d[0][len(s)-1]