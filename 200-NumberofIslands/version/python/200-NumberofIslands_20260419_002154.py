# Last updated: 4/19/2026, 12:21:54 AM
1'''
2Time Complexity: O(m*n)
3Space Complexity: O(m*n)
4'''
5class Solution:
6    def numIslands(self, grid: List[List[str]]) -> int:
7        count = 0
8        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
9        def dfs(i, j):
10            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == "0":
11                return
12            grid[i][j] = "0"
13            for d1, d2 in dirs:
14                dfs(i+d1, j+d2)
15            return
16
17        for i in range(len(grid)):
18            for j in range(len(grid[0])):
19                if grid[i][j] == "1":
20                    count += 1
21                    dfs(i, j)
22        return count