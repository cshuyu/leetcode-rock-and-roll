# Last updated: 3/19/2026, 6:05:20 PM
1class Solution:
2    # Time Complexity: O(V+E)--> O(K^n)
3    # Space Complexity: O(E)--> O(K^n)
4    def crackSafe(self, n: int, k: int) -> str:
5        starter = "0"*n
6        visited = set()
7        visited.add(starter)
8        path = []
9
10        def dfs(edge):
11            for i in range(k):
12                prefix = edge[1:]
13                next_edge = prefix + str(i)
14                if next_edge in visited:
15                    continue
16                visited.add(next_edge)
17                dfs(next_edge)
18                path.append(str(i))
19        
20        dfs(starter)
21        return "".join(path)+starter
22
23
24
25
26
27