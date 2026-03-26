# Last updated: 3/26/2026, 12:46:47 PM
# Minimum Spanning Tree: Kruskal Algorithm
1class UnionFind:
2    def __init__(self, n):
3        self.parents = list(range(n))
4        self.ranks = [0]*n
5    
6    def find(self, node):
7        if self.parents[node] != node:
8            self.parents[node] = self.find(self.parents[node])
9        return self.parents[node]
10
11    def union(self, u, v):
12        parent_u = self.find(u)
13        parent_v = self.find(v)
14        # return True if it is connected
15        if parent_u == parent_v:
16            return False
17        elif self.ranks[parent_u] < self.ranks[parent_v]:
18            self.parents[parent_u] = parent_v
19        elif self.ranks[parent_u] > self.ranks[parent_v]:
20            self.parents[parent_v] = parent_u
21        else:
22            self.parents[parent_u] = parent_v
23            self.ranks[parent_v] += 1
24        return True
25
26
27class Solution:
28    def minCostConnectPoints(self, points: List[List[int]]) -> int:
29        uf = UnionFind(len(points))
30        mst = 0
31        edge_count = 0
32        connections = []
33        for i in range(len(points)):
34            for j in range(i+1, len(points)):
35                weight = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
36                connections.append((i, j, weight))
37        
38        connections.sort(key=lambda x: x[2])
39        
40        for u, v, weight in connections:
41            if uf.union(u, v):
42                mst += weight
43                edge_count += 1
44        
45        if edge_count == len(points)-1:
46            return mst
47        else:
48            return -1
49                    
50
51                
52            
53
54
55