# Last updated: 4/17/2026, 5:28:47 PM
# DFS: Island Topic
1'''
2Time Complexity: O(m*n)
3Space Complexity: O(m*n)
4'''
5class Solution:
6    def numIslands(self, grid: List[List[str]]) -> int:
7        count = 0
8        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
9        def dfs(i, j):
10            if grid[i][j] == "0":
11                return
12            grid[i][j] = "0"
13            for d1, d2 in dirs:
14                if i+d1>=0 and j+d2>=0 and i+d1<len(grid) and j+d2<len(grid[0]):
15                    dfs(i+d1, j+d2)
16            return
17
18        for i in range(len(grid)):
19            for j in range(len(grid[0])):
20                if grid[i][j] == "1":
21                    count += 1
22                    dfs(i, j)
23        return count