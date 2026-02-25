# Last updated: 2/24/2026, 6:01:27 PM
# Graph->Traverse a graph(DFS)
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        if not heights: return []
4        
5        ROWS, COLS = len(heights), len(heights[0])
6        pac_visited = set()
7        atl_visited = set()
8        
9        def dfs(r, c, visited, prev_height):
10            # 1. Base Cases
11            if (
12                (r, c) in visited or       # Already visited this cell in this specific ocean's search
13                r < 0 or c < 0 or          # Out of bounds
14                r == ROWS or c == COLS or  # Out of bounds
15                heights[r][c] < prev_height # Water can't flow uphill (so reverse-water can't go to lower cells)
16            ):
17                return
18            
19            # 2. Mark as visited
20            visited.add((r, c))
21            
22            # 3. Explore neighbors (Up, Down, Left, Right)
23            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
24            for dr, dc in directions:
25                dfs(r + dr, c + dc, visited, heights[r][c])
26
27        # 1. Run DFS for Pacific (Top and Left edges)
28        for c in range(COLS):
29            dfs(0, c, pac_visited, heights[0][c])        # Top edge
30            dfs(ROWS - 1, c, atl_visited, heights[ROWS - 1][c]) # Bottom edge (Atlantic)
31
32        # 2. Run DFS for Atlantic (Bottom and Right edges)
33        for r in range(ROWS):
34            dfs(r, 0, pac_visited, heights[r][0])        # Left edge
35            dfs(r, COLS - 1, atl_visited, heights[r][COLS - 1]) # Right edge (Atlantic)
36
37        # 3. Find the Intersection (Cells reachable by BOTH)
38        # In Python, the `&` operator finds the intersection of two sets
39        return list(pac_visited & atl_visited)
40
41