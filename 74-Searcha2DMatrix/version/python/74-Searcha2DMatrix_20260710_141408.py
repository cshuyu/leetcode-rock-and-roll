# Last updated: 7/10/2026, 2:14:08 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        if not matrix or matrix[0] == 0:
4            return False
5        row_len = len(matrix)
6        col_len = len(matrix[0])
7        left = 0
8        right = row_len*col_len-1
9        while left<=right:
10            mid = left + (right-left)//2
11            check_row = mid // col_len
12            check_col = mid % col_len
13            if matrix[check_row][check_col]==target:
14                return True
15            elif matrix[check_row][check_col]<target:
16                left = mid+1
17            else:
18                right = mid-1
19        return False
20