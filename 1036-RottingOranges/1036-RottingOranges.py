# Last updated: 2/23/2026, 6:44:50 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((0,1), (0, -1), (-1, 0), (1, 0))
        fresh_cnt = 0
        node_queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    node_queue.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh_cnt += 1

        if fresh_cnt == 0:
            return 0
        max_step = 0

        while node_queue:
            x, y, step = node_queue.popleft()
            max_step = step
            for dir in dirs:
                x_step, y_step = dir
                x_next = x+x_step
                y_next = y+y_step
                if 0<=x_next<rows and 0<=y_next<cols and grid[x_next][y_next] == 1:
                    grid[x_next][y_next] = 2
                    fresh_cnt -= 1
                    node_queue.append((x_next, y_next, step+1))
        
        return max_step if fresh_cnt == 0 else -1
            


        
        