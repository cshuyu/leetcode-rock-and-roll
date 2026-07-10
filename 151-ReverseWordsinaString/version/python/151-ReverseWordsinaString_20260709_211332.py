# Last updated: 7/9/2026, 9:13:32 PM
# reverse_string
1"""
2If string is mutable in python, this solution can solve the problem in-place with O(1) space
3"""
4class Solution:
5    def reverseWords(self, s: str) -> str:
6        # Normalize the spaces
7        char_lst = list(" ".join(s.split()))
8
9        def reverse(char_lst, start, end):
10            left = start
11            right = end
12            while left<right:
13                char_lst[left], char_lst[right] = char_lst[right], char_lst[left]
14                left += 1
15                right -= 1
16        
17        reverse(char_lst, 0, len(char_lst)-1)
18        left = right = 0
19
20        for right in range(len(char_lst)):
21            if char_lst[right] == " ":
22                reverse(char_lst, left, right-1)
23                left = right+1
24            elif right == len(char_lst)-1:
25                reverse(char_lst, left, right)
26
27        return "".join(char_lst)
28