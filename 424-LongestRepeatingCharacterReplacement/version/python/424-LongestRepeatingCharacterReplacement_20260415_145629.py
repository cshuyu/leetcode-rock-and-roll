# Last updated: 4/15/2026, 2:56:29 PM
# Sliding Window
1'''
2Time Complexity: O(n)
3Space Complexity: O(1)
4'''
5class Solution:
6    def characterReplacement(self, s: str, k: int) -> int:
7        left = right = 0
8        maxFeq = 0
9        count = {}
10        maxLength = 0
11        while right<len(s):
12            rightChar = s[right]
13            count[rightChar] = count.get(rightChar, 0)+1
14            maxFeq = max(count[rightChar], maxFeq)
15            right += 1
16            if right-left-maxFeq>k:
17                leftChar = s[left]
18                count[leftChar] -= 1
19                left += 1
20            else:
21                maxLength = max(maxLength, right-left)
22        
23        return maxLength
24
25
26