# Last updated: 3/26/2026, 3:26:49 PM
# Minimum Spanning Tree: Kruskal algorithm
1'''
2Time Complexity:
31) sort: O(ElogE)
42) union: E*alphaO(E)
5Total will be O(ElogE)
6Space Complexity:
71) sort: O(E)
82) union: O(n)
9Total will be O(n+E)
10'''
11class UnionFind:
12    def __init__(self, n):
13        self.parents = list(range(0, n+1))
14        self.ranks = [0]*(n+1)
15    
16    def find(self, node):
17        if self.parents[node] != node:
18            self.parents[node] = self.find(self.parents[node])
19        return self.parents[node]
20    
21    def union(self, u, v):
22        parent_u = self.find(u)
23        parent_v = self.find(v)
24        if parent_u == parent_v:
25            return False
26        if self.ranks[parent_u] < self.ranks[parent_v]:
27            self.parents[parent_u] = parent_v
28        elif self.ranks[parent_u] > self.ranks[parent_v]:
29            self.parents[parent_v] = parent_u
30        else:
31            self.parents[parent_u] = parent_v
32            self.ranks[parent_v] += 1
33        return True
34
35class Solution:
36    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
37        connections.sort(key=lambda x: x[2])
38        uf = UnionFind(n)
39        mst = 0
40        edge_count = 0
41        for u, v, weight in connections:
42            if uf.union(u, v):
43                mst += weight
44                edge_count += 1
45        
46        if edge_count == n-1:
47            return mst
48        else:
49            return -1
50