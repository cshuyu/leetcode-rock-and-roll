# Last updated: 4/20/2026, 2:26:20 PM
1class Solution:
2    def numEnclaves(self, grid: List[List[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
6        count = 0
7
8        def dfs(i, j, isBorder):
9            count = 0
10            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
11                return count
12            if grid[i][j]==1:
13                if not isBorder:
14                    count += 1
15                grid[i][j] = 0
16            for dir in dirs:
17                count += dfs(i+dir[0], j+dir[1], isBorder)
18            return count
19
20        for i in range(m):
21            dfs(i, 0, True)
22            dfs(i, n-1, True)
23        for j in range(n):
24            dfs(0, j, True)
25            dfs(m-1, j, True)
26        for i in range(m):
27            for j in range(n):
28                if grid[i][j] == 1:
29                    count += dfs(i, j, False)
30        return count