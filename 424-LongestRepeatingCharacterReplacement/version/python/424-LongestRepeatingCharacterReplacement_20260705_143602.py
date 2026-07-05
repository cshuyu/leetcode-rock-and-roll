# Last updated: 7/5/2026, 2:36:02 PM
# Sliding Window
1"""
2Actually this question can be transferred to find longest same char within window size
3right pointer is exclusive.
4left pointer is inclusive.
5Space is O(1), since it saves the characters.
6"""
7class Solution:
8    def characterReplacement(self, s: str, k: int) -> int:
9        left = right = 0
10        charFreq = defaultdict(int)
11        maxFreq = 0
12        maxLength = 0
13
14        while right<len(s):
15            right_count = charFreq[s[right]]+1
16            charFreq[s[right]] = right_count
17            maxFreq = max(maxFreq, right_count)
18            right += 1
19
20            while right-left-maxFreq>k: 
21                charFreq[s[left]] = charFreq[s[left]]-1
22                left += 1
23            
24            maxLength = max(right-left, maxLength)
25        
26        return maxLength
27            
28