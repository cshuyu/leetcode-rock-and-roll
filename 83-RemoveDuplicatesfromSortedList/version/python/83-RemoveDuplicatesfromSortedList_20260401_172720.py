# Last updated: 4/1/2026, 5:27:20 PM
# Two Pointers: Reverse String
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        left = 0
7        right = len(s)-1
8        while left<right:
9            s[left], s[right] = s[right], s[left]
10            left += 1
11            right -= 1