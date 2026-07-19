# Last updated: 7/18/2026, 11:24:18 PM
# Backtracking: Palindrome
1"""
2O(Time): O(2^n*n), "s[start:i+1]" string's slicing operation complexity is O(n)
3O(Space): O(n)
4"""
5class Solution:
6    def partition(self, s: str) -> List[List[str]]:
7        res = []
8        curr_lst = []
9
10        def helper(start):
11            if start == len(s):
12                res.append(curr_lst.copy())
13                return
14            for i in range(start, len(s)):
15                curr_str = s[start:i+1]
16                if curr_str == curr_str[::-1]:
17                    curr_lst.append(curr_str)
18                    helper(i+1)
19                    curr_lst.pop()
20        helper(0)
21        return res
22