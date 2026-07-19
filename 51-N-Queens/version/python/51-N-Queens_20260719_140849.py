# Last updated: 7/19/2026, 2:08:49 PM
# Backtracking: Nqueen
1"""
2O(Time): O(n!)
3O(Space): O(n^2), board is O(n^2), the dicts and dfs stack is O(n)
4"""
5class Solution:
6    def solveNQueens(self, n: int) -> List[List[str]]:
7        res = []
8        board = [["."]*n for _ in range(n)]
9        cols = set()
10        diags1 = set()
11        diags2 = set()
12
13        def boardTransfer(board):
14            str_lst = []
15            for row in board:
16                str_lst.append("".join(row))
17            return str_lst
18
19        def helper(r):
20            if r == n:
21                res.append(boardTransfer(board))
22                return
23            for c in range(n):
24                if c not in cols and (r+c) not in diags1 and (r-c) not in diags2:
25                        cols.add(c)
26                        diags1.add(r+c)
27                        diags2.add(r-c)
28                        board[r][c] = "Q"
29                        helper(r+1)
30                        cols.remove(c)
31                        diags1.remove(r+c)
32                        diags2.remove(r-c)
33                        board[r][c] = "."
34        
35        helper(0)
36        return res
37