# Last updated: 7/12/2026, 12:17:03 AM
# 2D array
1"""
2Time: O(n)
3Space: O(1)
4"""
5class Solution:
6    def rotate(self, matrix: List[List[int]]) -> None:
7        """
8        Do not return anything, modify matrix in-place instead.
9        """
10        for i in range(len(matrix)):
11            for j in range(i, len(matrix[0])):
12                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
13
14        for row in matrix:
15            row.reverse()
16        
17        return matrix