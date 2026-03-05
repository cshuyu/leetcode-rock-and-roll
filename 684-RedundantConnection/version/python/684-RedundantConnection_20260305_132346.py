# Last updated: 3/5/2026, 1:23:46 PM
1class DSU:
2    def __init__(self, n):
3        self.n = n
4        self.parents = list(range(n))
5        self.rank = [1]*n
6    
7    def find(self, n):
8        if self.parents[n] == n:
9            return n
10        self.parents[n] = self.find(self.parents[n])
11        return self.parents[n]
12
13    def union(self, i, j):
14        root_i = self.find(i)
15        root_j = self.find(j)
16        if root_i == root_j:
17            return False
18        else:
19            if self.rank[root_i]>self.rank[root_j]:
20                self.parents[root_j] = root_i
21            elif self.rank[root_i]<self.rank[root_j]:
22                self.parents[root_i] = root_j
23            else:
24                self.parents[root_j] = root_i
25                self.rank[root_i] += 1
26            return True
27 
28
29class Solution:
30    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
31        dsu = DSU(len(edges)+1)
32        for u, v in edges:
33            if not dsu.union(u, v):
34                return [u, v]
35        