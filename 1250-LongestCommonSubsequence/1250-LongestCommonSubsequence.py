# Last updated: 2/23/2026, 6:44:44 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        if len1<=len2:
            text1, text2 = text2, text1
            len1, len2 = len2, len1

        prev_row = [0]*(len2+1)
        curr_row = [0]*(len2+1)

        for i in range(1, len1+1):
            curr_row = [0] * (len2 + 1)
            for j in range(1, len2+1):
                if text1[i-1]==text2[j-1]:
                    curr_row[j] = prev_row[j-1]+1
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j-1])
            prev_row = curr_row
        
        return curr_row[len2]