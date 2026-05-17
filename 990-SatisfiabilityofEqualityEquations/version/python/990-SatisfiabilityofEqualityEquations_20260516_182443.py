# Last updated: 5/16/2026, 6:24:43 PM
1'''
2Time Complexity: O(n)
3Space Complexity: O(1)
4'''
5class UnionFind:
6    def __init__(self, n):
7        self.parents = [i for i in range(n)]
8        self.ranks = [0]*n
9
10    def union(self, u, v):
11        parent_u = self.find(u)
12        parent_v = self.find(v)
13        if parent_u != parent_v:
14            if self.ranks[parent_u] < self.ranks[parent_v]:
15                self.parents[parent_u] = parent_v
16            elif self.ranks[parent_u] > self.ranks[parent_v]:
17                self.parents[parent_v] = parent_u
18            else:
19                self.parents[parent_v] = parent_u
20                self.ranks[parent_u] += 1
21
22    def find(self, node):
23        if self.parents[node] != node:
24            self.parents[node] = self.find(self.parents[node])
25        return self.parents[node]
26
27class Solution:
28    def equationsPossible(self, equations: List[str]) -> bool:
29        uf = UnionFind(26)
30        for equation in equations:
31            if equation[1] == "=":
32                u = ord(equation[0]) - ord("a")
33                v = ord(equation[3]) - ord("a")
34                uf.union(u, v)
35        
36        for equation in equations:
37            if equation[1] == "!":
38                u = ord(equation[0]) - ord("a")
39                v = ord(equation[3]) - ord("a")
40                if uf.find(u) == uf.find(v):
41                    return False
42        return True