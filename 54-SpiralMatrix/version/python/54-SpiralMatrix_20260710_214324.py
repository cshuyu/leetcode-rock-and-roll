# Last updated: 7/10/2026, 9:43:24 PM
# 2D array spiral traverse
1"""
2Time: O(m*n)
3Space: O(1)
4"""
5class Solution:
6    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
7        m = len(matrix)
8        n = len(matrix[0])
9        upper_bound = 0
10        lower_bound = m-1
11        left_bound = 0
12        right_bound = n-1
13        res = []
14        while len(res) < m*n:
15            if upper_bound <= lower_bound:
16                for i in range(left_bound, right_bound+1):
17                    res.append(matrix[upper_bound][i])
18                upper_bound += 1
19
20            if left_bound <= right_bound:
21                for j in range(upper_bound, lower_bound+1):
22                    res.append(matrix[j][right_bound])
23                right_bound -= 1
24            
25            if upper_bound <= lower_bound:
26                for i in range(right_bound, left_bound-1, -1):
27                    res.append(matrix[lower_bound][i])
28                lower_bound -= 1
29            
30            if left_bound <= right_bound:
31                for j in range(lower_bound, upper_bound-1, -1):
32                    res.append(matrix[j][left_bound])
33                left_bound += 1
34        return res
35                  