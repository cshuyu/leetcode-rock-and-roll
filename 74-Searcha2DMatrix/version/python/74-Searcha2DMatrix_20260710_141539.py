# Last updated: 7/10/2026, 2:15:39 PM
# Binary Search: 2D array
1"""
2O(Time): O(logm*n)
3O(Space): O(1)
4"""
5class Solution:
6    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
7        if not matrix or matrix[0] == 0:
8            return False
9        row_len = len(matrix)
10        col_len = len(matrix[0])
11        left = 0
12        right = row_len*col_len-1
13        while left<=right:
14            mid = left + (right-left)//2
15            check_row = mid // col_len
16            check_col = mid % col_len
17            if matrix[check_row][check_col]==target:
18                return True
19            elif matrix[check_row][check_col]<target:
20                left = mid+1
21            else:
22                right = mid-1
23        return False
24