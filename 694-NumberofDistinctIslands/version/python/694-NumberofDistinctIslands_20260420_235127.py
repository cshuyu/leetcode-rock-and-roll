# Last updated: 4/20/2026, 11:51:27 PM
# DFS with island problem of path combinations
1'''
2The path combination's time complexity won't over 2*m*n, space complexity won't over m*n
3The DFS's time complexity is 4*m*n, space complexity won't over m*n
4Therefore the total time and space complexity are both O(mn)
5'''
6class Solution:
7    def numDistinctIslands(self, grid: List[List[int]]) -> int:
8        m = len(grid)
9        n = len(grid[0])
10        valid_combinations = set()
11        dirs = [(-1, 0 , "l"), (1, 0, "r"), (0, -1, "d"), (0, 1, "u")]
12
13        def dfs(i, j, combinations):
14            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
15                return
16            grid[i][j]=0
17            for dx, dy, dir in dirs:
18                combinations.append(dir)
19                dfs(i+dx, j+dy, combinations)
20                # use "b" to show backtracking
21                combinations.append("b")
22
23        for i in range(m):
24            for j in range(n):
25                if grid[i][j] == 1:
26                    # use "s" to show the start
27                    combinations = []
28                    combinations.append("s")
29                    dfs(i, j, combinations)
30                    valid_combinations.add("".join(combinations))
31        return len(valid_combinations)
32                    
33