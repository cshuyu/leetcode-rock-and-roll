# Last updated: 3/4/2026, 3:16:25 PM
# Graph: Traverse with Eulerain path(DFS)
1class Solution:
2    def crackSafe(self, n: int, k: int) -> str:
3        start_node = "0"*(n-1)
4        visited = set()
5        path = []
6        # Complexity: there are k^(n-1) nodes and k^n edges
7        # We will go through k^n edges, 
8        # each of them will cost O(n) time, total is O(nk^n)~O(k^n) time
9        # The DFS stack space worst case is k^n
10        # The visited save all edges' possbilities, k^n possibilities
11        # each edge string's length is n, total is O(nk^n)~O(k^n) space
12        def dfs(node):
13            for i in range(k):
14                char = str(i)
15                edge = node+char
16                if edge not in visited:
17                    # Edge cost O(n) space
18                    visited.add(edge)
19                    # This operation cost O(n) time
20                    next_node = edge[1:]
21                    dfs(next_node)
22                    path.append(char)
23        
24        dfs(start_node)
25        path.reverse()
26        return start_node + "".join(path)
27