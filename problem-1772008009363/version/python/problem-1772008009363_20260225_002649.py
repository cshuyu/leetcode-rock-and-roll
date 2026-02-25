# Last updated: 2/25/2026, 12:26:49 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows = len(heights)
4        cols = len(heights[0])
5        pacific_visited = set()
6        atlantic_visited = set()
7
8        def dfs(r, c, visited, prev_height):
9            if ((r, c) in visited or 
10            r<0 or c<0 or r==rows or c==cols or
11            heights[r][c]<prev_height):
12                return
13
14            visited.add((r,c))
15
16            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
17            for dr, dc in directions:
18                dfs(r+dr, c+dc, visited, heights[r][c])
19        
20        for c in range(cols):
21            dfs(0, c, pacific_visited, heights[0][c])
22            dfs(rows-1, c, atlantic_visited, heights[rows-1][c])
23
24        for r in range(rows):
25            dfs(r, 0, pacific_visited, heights[r][0])
26            dfs(r, cols-1, atlantic_visited, heights[r][cols-1])
27
28        return list(pacific_visited & atlantic_visited)
29
30
31        