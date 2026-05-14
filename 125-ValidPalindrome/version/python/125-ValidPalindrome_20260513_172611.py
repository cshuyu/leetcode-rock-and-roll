# Last updated: 5/13/2026, 5:26:11 PM
1class Solution:
2    def isChar(c):
3        c = ord(c)
4        if c >= ord('a') and c <= ord('z'):
5            return True
6        if c >= ord('A') and c <= ord('Z'):
7            return True
8        if c >= ord('0') and c <= ord('9'):
9            return True
10        return False
11            
12    def isPalindrome(self, s: str) -> bool:
13        left = 0
14        right = len(s) - 1
15        while left < right:
16            while not s[left].isalnum() and left < right:
17                left += 1
18            while not s[right].isalnum() and left < right:
19                right -= 1
20            
21            if left < right and s[left].lower() != s[right].lower():
22                # print(f"{left} vs {right} vs {s[left]} {s[right]}")
23                return False
24            left+= 1
25            right -= 1
26        
27        return True