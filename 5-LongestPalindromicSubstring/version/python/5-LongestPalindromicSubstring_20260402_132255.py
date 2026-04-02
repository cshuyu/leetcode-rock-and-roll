# Last updated: 4/2/2026, 1:22:55 PM
# Two Pointers: Palindrome
1'''
2Time Complexity is O(n^2)
3Space Complexity is O(1)
4'''
5class Solution:
6    def longestPalindrome(self, s: str) -> str:
7        res = ""
8        for i in range(len(s)):
9            s1 = self.getPalindrome(s, i, i)
10            if i+1 < len(s):
11                s2 = self.getPalindrome(s, i, i+1)
12                res = s2 if len(s2)>len(res) else res
13            res = s1 if len(s1)>len(res) else res
14        return res
15    
16    def getPalindrome(self, s, index1, index2):
17        while index1>=0 and index2<len(s) and s[index1] == s[index2]:
18            index1 -= 1
19            index2 += 1
20        return s[index1+1:index2]