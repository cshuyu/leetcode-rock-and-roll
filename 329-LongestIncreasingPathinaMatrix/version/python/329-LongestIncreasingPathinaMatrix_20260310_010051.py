# Last updated: 3/10/2026, 1:00:51 AM
# Matrix: DFS+Memory
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        # Time Complexity: O(V+E)
4        # Space Complexity: O(V)
5        if not matrix or not matrix[0]:
6            return 0
7        rows, cols = len(matrix), len(matrix[0])
8        memo = [[0] * cols for _ in range(rows)]
9
10        def dfs(r, c):
11            if memo[r][c] != 0:
12                return memo[r][c]
13            longest = 1
14            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
15                nr, nc = r+dr, c+dc
16
17                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
18                    longest = max(longest, 1+dfs(nr, nc))
19            
20            memo[r][c] = longest
21            return longest
22
23        return max(dfs(r, c) for r in range(rows) for c in range(cols))