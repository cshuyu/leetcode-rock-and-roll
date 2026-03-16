# Last updated: 3/16/2026, 4:07:49 PM
# Graph: Union-Find solution
1# Union-Find Time Complexity: E*O(V), find is O(E), union is O(V).
2# In this question, O(E) is O(1), so time complexity is also O(V). 
3# Union-Find Space Complexity: O(V)
4class UnionFind:
5    def __init__(self, nums):
6        self.parent = {}
7        self.size = {}
8        if not nums:
9            self.max_size = 0
10        else:
11            self.max_size = 1
12        for num in nums:
13            self.parent[num] = num
14            self.size[num] = 1
15    
16    def find(self, node):
17        if self.parent[node]!=node:
18            self.parent[node]=self.find(self.parent[node])
19        return self.parent[node]
20    
21    def union(self, u, v):
22        p1 = self.find(u)
23        p2 = self.find(v)
24        if p1==p2:
25            return
26        if self.size[p1]<=self.size[p2]:
27            self.parent[p1] = p2
28            self.size[p2] += self.size[p1]
29        else:
30            self.parent[p2] = p1
31            self.size[p1] += self.size[p2]
32        curr_max_size = max(self.size[p1], self.size[p2])
33        self.max_size = max(self.max_size, curr_max_size)
34        return
35
36class Solution:
37    def longestConsecutive(self, nums: List[int]) -> int:
38        num_set = set(nums)
39        uf = UnionFind(num_set)
40
41        for num in num_set:
42            if num+1 in num_set:
43                uf.union(num, num+1)
44        
45        return uf.max_size
46
47        
48