# Last updated: 3/8/2026, 12:48:02 AM
1class Solution:
2    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
3        graph = defaultdict(list)
4        indegree = defaultdict(int)
5        outdegree = defaultdict(int)
6        path = []
7
8        for u, v in pairs:
9            graph[u].append(v)
10            indegree[v] += 1
11            outdegree[u] += 1
12        
13        def findStartNode():
14            for i in graph:
15                if outdegree[i]-indegree[i] == 1:
16                    return i
17            return pairs[0][0]
18        
19        def dfs(node):
20            next_lst = graph[node]
21            while next_lst:
22                next = next_lst.pop()
23                dfs(next)
24            path.append(node)
25        
26        dfs(findStartNode())
27        path.reverse()
28
29        res = []
30        for i in range(len(path)-1):
31            res.append([path[i], path[i+1]])
32        return res
33
34
35            
36