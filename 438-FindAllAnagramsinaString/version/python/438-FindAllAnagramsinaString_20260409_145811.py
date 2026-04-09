# Last updated: 4/9/2026, 2:58:11 PM
# Sliding Window
1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        targetMap = {}
4        wordMap = {}
5        for char in p:
6            targetMap[char] = targetMap.get(char, 0)+1
7        left = right = 0
8        valid = 0
9        res = []
10
11        while right<len(s):
12            curr = s[right]
13            if curr in targetMap:
14                wordMap[curr] = wordMap.get(curr, 0)+1
15                if wordMap[curr] == targetMap[curr]:
16                    valid += 1
17            right += 1
18            if right-left ==len(p):
19                if valid == len(targetMap):
20                    res.append(left)
21                leftChar = s[left]
22                if leftChar in wordMap:
23                    if wordMap[leftChar] == targetMap[leftChar]:
24                        valid -=1
25                    wordMap[leftChar] -= 1
26                left += 1
27        
28        return res
29
30