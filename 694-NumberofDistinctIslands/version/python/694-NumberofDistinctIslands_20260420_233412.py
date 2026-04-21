# Last updated: 4/20/2026, 11:34:12 PM
# DFS with island problem of dir combinations
1class Solution:
2    def numDistinctIslands(self, grid: List[List[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        valid_combinations = set()
6        dirs = [(-1, 0 , "l"), (1, 0, "r"), (0, -1, "d"), (0, 1, "u")]
7
8        def dfs(i, j, combinations):
9            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
10                return
11            grid[i][j]=0
12            for dx, dy, dir in dirs:
13                combinations.append(dir)
14                dfs(i+dx, j+dy, combinations)
15                # use "b" to show backtracking
16                combinations.append("b")
17
18        for i in range(m):
19            for j in range(n):
20                if grid[i][j] == 1:
21                    # use "s" to show the start
22                    combinations = []
23                    combinations.append("s")
24                    dfs(i, j, combinations)
25                    valid_combinations.add("".join(combinations))
26        return len(valid_combinations)
27                    
28