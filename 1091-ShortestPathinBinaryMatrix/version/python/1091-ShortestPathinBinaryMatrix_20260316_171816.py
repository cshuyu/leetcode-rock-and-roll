# Last updated: 3/16/2026, 5:18:16 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        # Time complexity is O(n^2)
4        # Space complexity is O(n^2)
5        if not grid or grid[0][0] != 0:
6            return -1  
7        # x, y, count
8        queue = deque([(0, 0, 1)])
9        grid[0][0] = 1
10        while queue:
11            curr_x, curr_y, count = queue.popleft()
12            if curr_x == len(grid)-1 and curr_y == len(grid[0])-1:
13                return count
14            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
15            for x, y in dirs:
16                next_x, next_y = curr_x+x, curr_y+y
17                if 0<=next_x<len(grid) and 0<=next_y<len(grid[0]) and grid[next_x][next_y]==0:
18                    queue.append((next_x, next_y, count+1))
19                    grid[next_x][next_y] = 1
20        return -1