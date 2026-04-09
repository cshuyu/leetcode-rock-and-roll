# Last updated: 4/8/2026, 5:28:18 PM
# Sliding window: minimum subarray
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        required = {}
4        curr_word = {}
5        for char in t:
6            required[char] = required.get(char, 0)+1
7        left = 0
8        right = 0
9        valid = 0
10        length = float("inf")
11        start = 0
12
13        while right<len(s):
14            curr_char = s[right]
15            if curr_char in required:
16                curr_word[curr_char] = curr_word.get(curr_char, 0)+1
17                if curr_word[curr_char] == required[curr_char]:
18                    valid += 1
19            right += 1
20            while valid == len(required):
21                if right-left<length:
22                    length = right-left
23                    start = left
24                curr_char = s[left]
25                if curr_char in curr_word:
26                    if curr_word[curr_char] == required[curr_char]:
27                        valid -= 1
28                    curr_word[curr_char] -= 1
29                left += 1
30        
31        return "" if length == float("inf") else s[start:start+length]
32