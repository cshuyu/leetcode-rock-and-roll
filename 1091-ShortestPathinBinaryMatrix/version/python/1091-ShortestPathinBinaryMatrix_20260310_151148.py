# Last updated: 3/10/2026, 3:11:48 PM
# Shortest Path with no weight: BFS
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        # Complexity of time is O(V+E), V is n^2, E is 8*n^2, total is still O(n^2)
4        # Complexity of space is also O(n^2)
5        # Check if start or end is blocked
6        n = len(grid)
7        if grid[0][0]==1 or grid[n-1][n-1]==1:
8            return -1
9
10        # Queue stores (row, col, distance)
11        queue = deque([(0, 0, 1)])
12        grid[0][0] = 1
13
14        directions = [
15            (-1, -1), (-1, 0), (-1, 1),
16            (0, -1),            (0, 1),
17            (1, -1), (1, 0), (1,1)
18        ]
19
20        while queue:
21            r, c, dist = queue.popleft()
22
23            # Found the destination
24            if r==n-1 and c==n-1:
25                return dist
26
27            for dr, dc in directions:
28                nr, nc = r+dr, c+dc
29                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0:
30                    grid[nr][nc] = 1
31                    queue.append([nr, nc, dist+1])
32        
33        return -1
34