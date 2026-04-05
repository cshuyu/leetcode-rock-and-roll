# Last updated: 4/4/2026, 6:18:11 PM
# Graph: Dijkstra
1'''
2Time Complexity: O(ElogV) --> O(MNlogMN)
3Space Complexity: O(V) --> O(MN)
4'''
5class Solution:
6    def minCost(self, grid: List[List[int]]) -> int:
7        pointHeap = [(0, 0, 0)]
8        dirs = {1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]}
9        preCost = [[float("inf")]*len(grid[0]) for _ in range(len(grid))]
10        while pointHeap:
11            cost, row, col = heapq.heappop(pointHeap)
12            if cost > preCost[row][col]:
13                continue
14            if row == len(grid)-1 and col == len(grid[0])-1:
15                return cost
16            for dir in dirs:
17                nr = row + dirs[dir][0]
18                nc = col + dirs[dir][1]
19                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
20                    if dir != grid[row][col]:
21                        curr_cost = cost + 1
22                    else:
23                        curr_cost = cost
24                    if curr_cost < preCost[nr][nc]:
25                        preCost[nr][nc] = curr_cost
26                        heapq.heappush(pointHeap, (curr_cost, nr, nc))
27        
28
29            
30