# Last updated: 3/16/2026, 12:56:03 PM
1class Solution:
2    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
3        # inOutDiff is out-in
4        inOutDiff = defaultdict(int)
5        graph = defaultdict(list)
6        for u, v in pairs:
7            inOutDiff[u] += 1
8            inOutDiff[v] -= 1
9            graph[u].append(v)
10        
11        start_node = pairs[0][0]
12        for node in inOutDiff:
13            if inOutDiff[node]>0:
14                start_node = node
15                break
16        
17        path = []
18        res = []
19        def visit(node):
20            while graph[node]:
21                next_node = graph[node].pop()
22                visit(next_node)
23            path.append(node)
24        
25        visit(start_node)
26        path.reverse()
27        for i in range(len(path)-1):
28            res.append([path[i], path[i+1]])
29
30        return res 
31
32
33
34