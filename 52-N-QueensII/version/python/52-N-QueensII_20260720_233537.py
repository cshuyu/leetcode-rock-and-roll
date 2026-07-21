# Last updated: 7/20/2026, 11:35:37 PM
# Backtracking: Nqueens
1"""
2O(Time): O(n!)
3O(Space): O(n)
4"""
5class Solution:
6    def totalNQueens(self, n: int) -> int:
7        cols = set()
8        diags1 = set()
9        diags2 = set()
10
11        def helper(r):
12            if r == n:
13                return 1
14            solutions = 0
15            for c in range(n):
16                if c not in cols and r+c not in diags1 and r-c not in diags2:
17                    cols.add(c)
18                    diags1.add(r+c)
19                    diags2.add(r-c)
20                    solutions += helper(r+1)
21                    cols.remove(c)
22                    diags1.remove(r+c)
23                    diags2.remove(r-c)
24            return solutions
25
26        return helper(0)
27