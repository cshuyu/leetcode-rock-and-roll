# Last updated: 2/23/2026, 6:44:22 PM
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        start_row = entrance[0]
        start_col = entrance[1]
        maze[start_row][start_col] = '+'
        node_queue = deque([[start_row, start_col, 0]])
        
        while node_queue:
            curr_node = node_queue.popleft()
            curr_row, curr_col, curr_distance = curr_node
            for dir in dirs:
                next_row = curr_row+dir[0]
                next_col = curr_col+dir[1]
                if 0<=next_row<row and 0<=next_col<col and maze[next_row][next_col] == ".":
                    if next_row == 0 or next_row == row-1 or next_col == 0 or next_col == col-1:
                        return curr_distance+1
                    maze[next_row][next_col] = "+"
                    node_queue.append([next_row, next_col, curr_distance+1])
        
        return -1










            
