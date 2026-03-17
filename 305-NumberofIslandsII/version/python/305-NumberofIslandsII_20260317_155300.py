# Last updated: 3/17/2026, 3:53:00 PM
1# Time Complexity: O(k)
2# Space Complexity: O(mn)
3class UnionFind:
4    def __init__(self, m, n):
5        self.rank = [0]*m*n
6        self.parents = list(range(m*n))
7    def find(self, index):
8        if self.parents[index] != index:
9            self.parents[index] = self.find(self.parents[index])
10        return self.parents[index]
11    def union(self, index1, index2):
12        p1 = self.find(index1)
13        p2 = self.find(index2)
14        if p1==p2:
15            return False
16        if self.rank[p1]<self.rank[p2]:
17            self.parents[p1] = p2
18        elif self.rank[p1]>self.rank[p2]:
19            self.parents[p2] = p1
20        else:
21            self.parents[p1] = p2
22            self.rank[p2] += 1
23        return True
24        
25class Solution:
26    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
27        count = 0
28        res = []
29        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
30        visited = set()
31        uf = UnionFind(m, n)
32        for r, c in positions:
33            index = n*r+c
34            if index in visited:
35                res.append(count)
36                continue
37            visited.add(index)
38            count += 1
39            for nr, nc in dirs:
40                neighbor_r = r+nr
41                neighbor_c = c+nc
42                neighbor_index = neighbor_r*n+neighbor_c
43                if 0<=neighbor_r<m and 0<=neighbor_c<n and neighbor_index in visited:
44                    if uf.union(index, neighbor_index):
45                        count -= 1
46            res.append(count)
47        
48        return res
49