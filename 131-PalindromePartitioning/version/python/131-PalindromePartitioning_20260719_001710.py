# Last updated: 7/19/2026, 12:17:10 AM
# backtracking with dp improvement
1"""
2O(Time): O(2^n*n), "s[start:i+1]" string's slicing operation complexity is O(n)
3O(Space): O(n)
4"""
5class Solution:
6    def partition(self, s: str) -> List[List[str]]:
7        res = []
8        curr_lst = []
9        n = len(s)
10        dp = [[False]*n for _ in range(n)]
11        for i in range(n-1,-1,-1):
12            for j in range(i, n):
13                if s[i] == s[j]:
14                    if j-i<=2 or dp[i+1][j-1]:
15                        dp[i][j] = True
16
17        def helper(start):
18            if start == len(s):
19                res.append(curr_lst.copy())
20                return
21            for i in range(start, len(s)):
22                curr_str = s[start:i+1]
23                if dp[start][i]:
24                    curr_lst.append(curr_str)
25                    helper(i+1)
26                    curr_lst.pop()
27        helper(0)
28        return res
29