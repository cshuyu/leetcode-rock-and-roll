# Last updated: 7/11/2026, 12:06:38 AM
# 2D array spiral traverse
1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        upper_bound = 0
4        lower_bound = n-1
5        left_bound = 0
6        right_bound = n-1
7        res = [[0]*n for i in range(n)]
8        num = 1
9        while left_bound<=right_bound and upper_bound<=lower_bound:
10            if upper_bound <= lower_bound:
11                for i in range(left_bound, right_bound+1):
12                    res[upper_bound][i] = num
13                    num += 1
14                upper_bound += 1
15            
16            if left_bound <= right_bound:
17                for j in range(upper_bound, lower_bound+1):
18                    res[j][right_bound] = num
19                    num += 1
20                right_bound -= 1
21            
22            if upper_bound <= lower_bound:
23                for i in range(right_bound, left_bound-1, -1):
24                    res[lower_bound][i] = num
25                    num += 1
26                lower_bound -= 1
27
28            if left_bound <= right_bound:
29                for j in range(lower_bound, upper_bound-1, -1):
30                    res[j][left_bound] = num
31                    num += 1
32                left_bound += 1
33        
34        return res
35