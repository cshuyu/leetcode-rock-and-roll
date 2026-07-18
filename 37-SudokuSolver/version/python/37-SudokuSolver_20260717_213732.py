# Last updated: 7/17/2026, 9:37:32 PM
# Backtracking
1"""
2O(Time): O(9^(n*n))
3O(Space): O(n*n)
4"""
5class Solution:
6    def solveSudoku(self, board: List[List[str]]) -> None:
7        """
8        Do not return anything, modify board in-place instead.
9        """
10        rows = [set() for _ in range(9)]
11        cols = [set() for _ in range(9)]
12        boxes = [set() for _ in range(9)]
13        
14        for r in range(9):
15            for c in range(9):
16                if board[r][c] != ".":
17                    char = board[r][c]
18                    rows[r].add(char)
19                    cols[c].add(char)
20                    box_idx = (r//3) * 3 + (c//3)
21                    boxes[box_idx].add(char)        
22
23        def helper(r, c):
24            if r == 9:
25                return True
26            if c == 9:
27                return helper(r+1, 0)
28            if board[r][c] != ".":
29                return helper(r, c+1)
30
31            box_idx = (r//3) * 3 + (c//3)
32            for i in map(str, range(1, 10)):
33                if i not in rows[r] and i not in cols[c] and i not in boxes[box_idx]:
34                    board[r][c] = i
35                    rows[r].add(i)
36                    cols[c].add(i)
37                    boxes[box_idx].add(i)
38
39                    if helper(r, c+1):
40                        return True
41
42                    board[r][c] = "."
43                    rows[r].remove(i)
44                    cols[c].remove(i)
45                    boxes[box_idx].remove(i)
46
47            return False
48        
49        helper(0, 0)
50
51                       