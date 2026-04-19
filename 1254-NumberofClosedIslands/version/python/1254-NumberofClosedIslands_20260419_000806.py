# Last updated: 4/19/2026, 12:08:06 AM
# DFS with Border Process
1'''
2Time Complexity: O(mn)
3Space Complexity: O(mn)
4'''
5class Solution:
6    def closedIsland(self, grid: List[List[int]]) -> int:
7        m = len(grid)
8        n = len(grid[0])
9        count = 0
10        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
11
12        def dfs(i, j):
13            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 1:
14                return
15            grid[i][j] = 1
16            for dir in dirs:
17                dfs(i+dir[0], j+dir[1])
18                        
19        for i in range(m):
20            dfs(i, 0)
21            dfs(i, n-1)
22        for j in range(n):
23            dfs(0, j)
24            dfs(m-1, j)
25        for i in range(m):
26            for j in range(n):
27                if grid[i][j] == 0:
28                    count += 1
29                    dfs(i, j)
30        return count
31                