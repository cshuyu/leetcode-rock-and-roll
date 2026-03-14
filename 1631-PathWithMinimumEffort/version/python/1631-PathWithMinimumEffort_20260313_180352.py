# Last updated: 3/13/2026, 6:03:52 PM
# Shortest Path, min-max problem
1class Solution:
2    def minimumEffortPath(self, heights: List[List[int]]) -> int:
3        min_effort = [[float('inf')]*len(heights[0]) for _ in range(len(heights))]
4        min_heap = [(0, 0, 0)]
5        while min_heap:
6            curr_effort, curr_i, curr_j = heapq.heappop(min_heap)
7            dirs = [(-1, 0), (1, 0), (0,-1), (0,1)]
8            if curr_effort > min_effort[curr_i][curr_j]:
9                continue
10            if curr_i == len(heights)-1 and curr_j == len(heights[0])-1:
11                return curr_effort
12            for dir in dirs:
13                next_i, next_j = curr_i+dir[0], curr_j+dir[1]
14                if 0<=next_i<len(heights) and 0<=next_j<len(heights[0]):
15                    edge_effort = abs(heights[next_i][next_j]-heights[curr_i][curr_j])
16                    next_effort = max(curr_effort, edge_effort)
17                    if next_effort<min_effort[next_i][next_j]:
18                        min_effort[next_i][next_j] = next_effort
19                        heapq.heappush(min_heap, (next_effort, next_i, next_j))
20        return min_effort[len(heights)-1][len(heights[0])-1]
21
22
23
24
25
26
27
28
29
30