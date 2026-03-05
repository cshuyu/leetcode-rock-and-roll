# Last updated: 3/5/2026, 11:50:32 AM
1class Solution:
2    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
3        # n nodes, labeled 1 to n
4        parent = list(range(len(edges) + 1))
5        
6        def find(i):
7            if parent[i] == i:
8                return i
9            # Path compression: point node directly to root
10            parent[i] = find(parent[i])
11            return parent[i]
12
13        def union(i, j):
14            root_i = find(i)
15            root_j = find(j)
16            if root_i != root_j:
17                parent[root_i] = root_j
18                return True
19            return False # They are already in the same set!
20
21        for u, v in edges:
22            if not union(u, v):
23                return [u, v]
24
25
26