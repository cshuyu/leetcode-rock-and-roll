# Last updated: 7/10/2026, 1:49:12 PM
# Top Corner Binary Search
1"""
2Time: O(m+n)
3Space: O(1)
4Pruning Search (the "Top-Right Corner" = "Binary Search Tree" approach)
5"""
6class Solution:
7    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
8        if not matrix or len(matrix[0])==0:
9            return False
10        col_len = len(matrix[0])
11        row_len = len(matrix)
12        row = 0
13        col = col_len-1
14        while row<row_len and col>=0:
15            if matrix[row][col] == target:
16                return True
17            elif matrix[row][col]<target:
18                row += 1
19            else:
20                col -= 1
21        return False