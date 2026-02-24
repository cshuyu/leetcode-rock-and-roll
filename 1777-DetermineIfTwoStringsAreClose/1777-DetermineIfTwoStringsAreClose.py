# Last updated: 2/23/2026, 6:44:29 PM
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wordMap1 = {}
        wordMap2 = {}
        for i in word1:
            wordMap1[i] = wordMap1.get(i, 0)+1
        for j in word2:
            wordMap2[j] = wordMap2.get(j, 0)+1
        if set(wordMap1.keys()) != set(wordMap2.keys()):
            return False
        if sorted(wordMap1.values()) == sorted(wordMap2.values()):
            return True
        else:
            return False

        