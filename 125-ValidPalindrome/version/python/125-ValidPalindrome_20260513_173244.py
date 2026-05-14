# Last updated: 5/13/2026, 5:32:44 PM
# Two Pointers
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        def isAlphanum(character):
4            c = ord(character)
5            if c >= ord("a") and c <= ord("z"):
6                return True
7            if c >= ord("A") and c <= ord("Z"):
8                return True
9            if c >= ord("0") and c <= ord("9"):
10                return True
11            return False
12
13        if not s:
14            return True
15        left = 0
16        right = len(s)-1
17        while left<right:
18            while not isAlphanum(s[left]) and left<len(s)-1:
19                left += 1
20            while not isAlphanum(s[right]) and right>0:
21                right -= 1
22            if left<right:
23                if s[left].lower() != s[right].lower():
24                    return False
25                if s[left].lower() == s[right].lower():
26                    left += 1
27                    right -= 1
28        return True
29