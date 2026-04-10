# Last updated: 4/9/2026, 11:47:49 PM
# Sliding Window
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = right = 0
4        words = set()
5        length = 0
6        while right<len(s):
7            currRight = s[right]
8            while currRight in words:
9                words.remove(s[left])
10                left += 1
11            words.add(currRight)
12            right += 1
13            if length < right-left:
14                length = right - left
15        return length
16
17
18