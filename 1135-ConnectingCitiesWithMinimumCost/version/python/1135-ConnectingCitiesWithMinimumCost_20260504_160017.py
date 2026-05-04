# Last updated: 5/4/2026, 4:00:17 PM
# Union_Find: 2nd try
1class UnionFind:
2    def __init__(self, n):
3        self.parents = list(range(n+1))
4        self.count = n
5        self.rank = [0]*(n+1)
6    
7    def find(self, i):
8        if self.parents[i]!=i:
9            self.parents[i] = self.find(self.parents[i])
10        return self.parents[i]
11    
12    def union(self, i, j):
13        parent_i = self.find(i)
14        parent_j = self.find(j)
15        if parent_i == parent_j:
16            return False
17        if self.rank[parent_i]<self.rank[parent_j]:
18            self.parents[parent_i] = parent_j
19        elif self.rank[parent_i]>self.rank[parent_j]:
20            self.parents[parent_j] = parent_i
21        else:
22            self.parents[parent_i] = parent_j
23            self.rank[parent_j] += 1
24        self.count -= 1
25        return True
26
27
28class Solution:
29    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
30        res = 0
31        connections.sort(key=lambda x: x[2])
32        uf = UnionFind(n)
33        for u, v, cost in connections:
34            if uf.union(u, v):
35                res += cost
36        if uf.count == 1:
37            return res
38        else:
39            return -1
40
41
42
43
44