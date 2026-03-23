# Last updated: 3/23/2026, 1:45:17 PM
# Minimum Spanning Tree: Kruskal Algorithm
1class UnionFind:
2    def __init__(self, n):
3        self.parents = list(range(0, n+1))
4        self.ranks = [0]*(n+1)
5    
6    def find(self, node):
7        if self.parents[node] != node:
8            self.parents[node] = self.find(self.parents[node])
9        return self.parents[node]
10    
11    def union(self, u, v):
12        parent_u = self.find(u)
13        parent_v = self.find(v)
14        if parent_u == parent_v:
15            return False
16        if self.ranks[parent_u] < self.ranks[parent_v]:
17            self.parents[parent_u] = parent_v
18        elif self.ranks[parent_u] > self.ranks[parent_v]:
19            self.parents[parent_v] = parent_u
20        else:
21            self.parents[parent_u] = parent_v
22            self.ranks[parent_v] += 1
23        return True
24
25class Solution:
26    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
27        connections.sort(key=lambda x: x[2])
28        uf = UnionFind(n)
29        mst = 0
30        edge_count = 0
31        for u, v, weight in connections:
32            if uf.union(u, v):
33                mst += weight
34                edge_count += 1
35        
36        if edge_count == n-1:
37            return mst
38        else:
39            return -1
40
41        