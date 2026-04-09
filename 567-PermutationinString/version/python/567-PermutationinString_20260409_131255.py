# Last updated: 4/9/2026, 1:12:55 PM
# Sliding Window with Fixed Size
1'''
2Time Complexity: O(m+n)
3Space Complexity: O(1)
4'''
5class Solution:
6    def checkInclusion(self, s1: str, s2: str) -> bool:
7        targetMap = {}
8        wordMap = {}
9        for char in s1:
10            targetMap[char] = targetMap.get(char, 0)+1
11
12        left = right = 0
13        valid = 0
14        while right<len(s2):
15            curr = s2[right]
16            if curr in targetMap:
17                wordMap[curr] = wordMap.get(curr, 0)+1
18                if wordMap[curr] == targetMap[curr]:
19                    valid += 1
20            right += 1
21            while right-left >= len(s1):
22                if valid == len(targetMap):
23                    return True
24                word = s2[left]
25                if word in targetMap :
26                    if wordMap[word]==targetMap[word]:
27                        valid -= 1
28                    wordMap[word] -= 1
29                left += 1
30        
31        return False