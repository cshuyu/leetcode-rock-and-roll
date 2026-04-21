# Last updated: 4/20/2026, 5:47:36 PM
# DFS with island problem, don't forget to keep doing DFS to mark the visited land, no matter if it is sub-island.
1class Solution:
2    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
3        m = len(grid1)
4        n = len(grid1[0])
5        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
6        count = 0
7
8        def isSub(i, j):
9            res = True
10            if i<0 or j<0 or i>=m or j>=n or grid2[i][j] == 0:
11                return True
12            if grid1[i][j] != 1:
13                res = False
14            grid2[i][j] = 0
15            for dir in dirs:
16                if not isSub(i+dir[0], j+dir[1]):
17                    res = False
18            return res
19
20        for i in range(m):
21            for j in range(n):
22                if grid2[i][j] == 1:
23                    if isSub(i, j):
24                        count += 1
25        return count