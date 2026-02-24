# Last updated: 2/23/2026, 6:44:26 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        word1_len = len(word1);
        word2_len = len(word2);
        common_len = min(word1_len, word2_len)
        for i in range(common_len):
            res += word1[i];
            res += word2[i];
        if word1_len > common_len:
            res += word1[common_len:word1_len]
        else:
            res += word2[common_len:word2_len]
        return res
        
        
            
        