# Last updated: 5/22/2026, 4:54:41 PM
# Binary Search
1'''
2Time: O(n*log(max-min))
3Space: O(1)
4'''
5class Solution:
6    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
7        max_row = len(matrix)
8        max_col = len(matrix[0])
9        left = matrix[0][0]
10        right = matrix[max_row-1][max_col-1]
11
12        def countLessVal(val):
13            row = max_row-1
14            col = 0
15            count = 0
16            while row>=0 and col<max_col:
17                if matrix[row][col] <= val:
18                    count += row+1
19                    col += 1
20                else:
21                    row -= 1
22            return count
23
24        while left<right:
25            mid = left + (right-left)//2
26            if countLessVal(mid) < k:
27                left = mid+1
28            else:
29                right = mid
30        return left        