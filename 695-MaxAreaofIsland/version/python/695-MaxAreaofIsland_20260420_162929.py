# Last updated: 4/20/2026, 4:29:29 PM
# DFS with Island Problem
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
6        max_count = 0
7
8        def dfs(i, j):
9            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
10                return 0
11            grid[i][j] = 0
12            count = 1
13            for dir in dirs:
14                count += dfs(i+dir[0], j+dir[1])
15            return count
16
17        for i in range(m):
18            for j in range(n):
19                if grid[i][j]==1:
20                    max_count = max(max_count, dfs(i, j))
21        return max_count