# Last updated: 3/26/2026, 1:30:45 PM
# Minimum Spanning Tree: Kruskal algorithm
1'''
2Time Complexity:
31) build graph: O(V!)
42) sort: O(E*logE)
53) union part: O(E*alpha(N))
6E equls n^2, so total is like O(n^2*log(n^2))
7Space Complexity:
81) union find array: O(n)
92) python sort space: O(n^2)<--worst case of quick sort
10Total is O(n^2)
11'''
12class UnionFind:
13    def __init__(self, n):
14        self.parents = list(range(n))
15        self.ranks = [0]*n
16    
17    def find(self, node):
18        if self.parents[node] != node:
19            self.parents[node] = self.find(self.parents[node])
20        return self.parents[node]
21
22    def union(self, u, v):
23        parent_u = self.find(u)
24        parent_v = self.find(v)
25        # return True if it is connected
26        if parent_u == parent_v:
27            return False
28        elif self.ranks[parent_u] < self.ranks[parent_v]:
29            self.parents[parent_u] = parent_v
30        elif self.ranks[parent_u] > self.ranks[parent_v]:
31            self.parents[parent_v] = parent_u
32        else:
33            self.parents[parent_u] = parent_v
34            self.ranks[parent_v] += 1
35        return True
36
37
38class Solution:
39    def minCostConnectPoints(self, points: List[List[int]]) -> int:
40        uf = UnionFind(len(points))
41        mst = 0
42        edge_count = 0
43        connections = []
44        for i in range(len(points)):
45            for j in range(i+1, len(points)):
46                weight = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
47                connections.append((i, j, weight))
48        
49        connections.sort(key=lambda x: x[2])
50        
51        for u, v, weight in connections:
52            if uf.union(u, v):
53                mst += weight
54                edge_count += 1
55        
56        if edge_count == len(points)-1:
57            return mst
58        else:
59            return -1
60