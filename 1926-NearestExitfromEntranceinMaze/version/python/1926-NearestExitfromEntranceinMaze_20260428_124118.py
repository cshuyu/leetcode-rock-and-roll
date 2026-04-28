# Last updated: 4/28/2026, 12:41:18 PM
1class Solution:
2    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
3        dq = deque()
4        dq.append((entrance[0], entrance[1], 0))
5        m = len(maze)
6        n = len(maze[0])
7        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
8        visited = [[False]*n for _ in range(m)]
9        visited[entrance[0]][entrance[1]] = True
10        while dq:
11            x, y, step = dq.popleft()
12            for dx, dy in dirs:
13                next_x = x+dx
14                next_y = y+dy
15                if next_x>=0 and next_x<m and next_y>=0 and next_y<n and maze[next_x][next_y]=="." and not visited[next_x][next_y]:
16                    if next_x==0 or next_y==0 or next_x==m-1 or next_y==n-1:
17                        return step+1
18                    dq.append((next_x, next_y, step+1))
19                    visited[next_x][next_y] = True
20        return -1
21