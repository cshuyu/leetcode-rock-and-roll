# Last updated: 4/17/2026, 1:16:35 PM
# 2D Array
1'''
2O(Time) is MNlog(min(m, n))
3O(Complexity) is MN
4'''
5class Solution:
6    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
7        diag_map = defaultdict(list)
8        for i in range(len(mat)):
9            for j in range(len(mat[0])):
10                diff = i-j
11                diag_map[diff].append(mat[i][j])
12
13        for diag in diag_map:
14            diag_map[diag].sort(reverse=True)
15        
16        for i in range(len(mat)):
17            for j in range(len(mat[0])):
18                mat[i][j] = diag_map[i-j].pop()
19        
20        return mat
21
22