# Last updated: 2/23/2026, 6:44:15 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        rm = {}
        cm = {}

        for i in range(r):
            row = tuple(grid[i])
            rm[row] = rm.get(row, 0)+1
        
        for i in range(c):
            column = []
            for j in range(r):
                column.append(grid[j][i])
            column = tuple(column)
            cm[column] = cm.get(column, 0)+1
        
        res = 0

        for pattern in rm:
            res += rm.get(pattern, 0) * cm.get(pattern, 0)
        
        return res
