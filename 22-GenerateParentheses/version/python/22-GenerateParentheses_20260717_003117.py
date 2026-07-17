# Last updated: 7/17/2026, 12:31:17 AM
# Backtracking
1"""
2O(Time): O(2^2n)
3O(Space): O(n)
4"""
5class Solution:
6    def generateParenthesis(self, n: int) -> List[str]:
7        res = []
8        curr_lst = []
9
10        def helper(left, right, curr_lst):
11            if left == 0 and right == 0:
12                res.append("".join(curr_lst))
13                return
14            if left>=1:
15                curr_lst.append("(")
16                helper(left-1, right, curr_lst)
17                curr_lst.pop()
18            if right>=1 and left<right:
19                curr_lst.append(")")
20                helper(left, right-1, curr_lst)
21                curr_lst.pop()
22        
23        helper(n, n, curr_lst)
24        return res
25
26