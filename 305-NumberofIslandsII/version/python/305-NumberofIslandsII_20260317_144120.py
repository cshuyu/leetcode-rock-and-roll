# Last updated: 3/17/2026, 2:41:20 PM
1class UnionFind:
2    def __init__(self, m, n):
3        self.rank = [0]*m*n
4        self.parents = list(range(m*n))
5    def find(self, index):
6        if self.parents[index] != index:
7            self.parents[index] = self.find(self.parents[index])
8        return self.parents[index]
9    def union(self, index1, index2):
10        p1 = self.find(index1)
11        p2 = self.find(index2)
12        if p1==p2:
13            return False
14        if self.rank[p1]<self.rank[p2]:
15            self.parents[p1] = p2
16        elif self.rank[p1]>self.rank[p2]:
17            self.parents[p2] = p1
18        else:
19            self.parents[p1] = p2
20            self.rank[p2] += 1
21        return True
22        
23class Solution:
24    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
25        count = 0
26        res = []
27        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
28        visited = set()
29        uf = UnionFind(m, n)
30        for r, c in positions:
31            index = n*r+c
32            if index in visited:
33                res.append(count)
34                continue
35            visited.add(index)
36            count += 1
37            for nr, nc in dirs:
38                neighbor_r = r+nr
39                neighbor_c = c+nc
40                neighbor_index = neighbor_r*n+neighbor_c
41                if 0<=neighbor_r<m and 0<=neighbor_c<n and neighbor_index in visited:
42                    if uf.union(index, neighbor_index):
43                        count -= 1
44            res.append(count)
45        
46        return res
47