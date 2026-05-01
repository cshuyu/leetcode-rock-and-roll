# Last updated: 5/1/2026, 2:08:23 PM
# BFS with matrix moves
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        dq = deque()
4        if grid[0][0] == 1:
5            return -1
6        if len(grid)==1:
7            return 1
8        dq.append((0, 0, 1))
9        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
10        grid[0][0] = 1
11
12        while dq:
13            curr_x, curr_y, steps = dq.popleft()
14            for dx, dy in dirs:
15                next_x = curr_x+dx
16                next_y = curr_y+dy
17                if next_x>=0 and next_x<len(grid) and next_y>=0 and next_y<len(grid[0]):
18                    if grid[next_x][next_y]!=1:
19                        if next_x==len(grid)-1 and next_y==len(grid[0])-1:
20                            return steps+1
21                        dq.append((next_x, next_y, steps+1))
22                        grid[next_x][next_y] = 1
23        
24        return -1