# Last updated: 3/6/2026, 8:25:31 PM
# Graph: Union Find with streaming new point
1class DNS:
2    def __init__(self, m, n):
3        self.parents = list(range(0, m*n))
4        self.ranks = [1]*(m*n)
5        self.counts = 0
6        self.is_island = set()
7    
8    def find(self, position):
9        if self.parents[position] != position:
10            self.parents[position] = self.find(self.parents[position])
11        return self.parents[position]    
12
13    def union(self, p1, p2):
14        root1 = self.find(p1)
15        root2 = self.find(p2)
16        if root1 != root2:
17            self.counts -= 1
18            if self.ranks[root1] < self.ranks[root2]:
19                self.parents[root1] = root2
20            elif self.ranks[root1] > self.ranks[root2]: 
21                self.parents[root2] = root1
22            else:
23                self.parents[root2] = root1
24                self.ranks[root1] += 1
25
26class Solution:
27    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
28        dns = DNS(m, n)
29        res = []
30        for r,c in positions:
31            curr = r*n+c
32            # corner case: there are duplicated points in positions
33            if curr in dns.is_island:
34                res.append(dns.counts)
35                continue
36            dns.counts += 1
37            dns.is_island.add(curr)
38            for next_dir in [[-1,0],[1, 0],[0, -1],[0, 1]]:
39                next_r = r+next_dir[0]
40                next_c = c+next_dir[1]
41                next = next_r * n + next_c
42                # always need to check the boundary before calculating the next
43                if (next_r>=0 and next_r<m and 
44                    next_c>=0 and next_c<n and
45                    next in dns.is_island):
46                    dns.union(curr, next)
47            res.append(dns.counts)
48        return res
49