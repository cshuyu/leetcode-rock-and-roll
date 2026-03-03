# Last updated: 3/3/2026, 2:48:08 PM
# Graph: Eulerain Path with starting node(DFS)
1class Solution:
2    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
3        # space: O(E)
4        graph = defaultdict(list)
5        indegree = defaultdict(int)
6        outdegree = defaultdict(int)
7        path_lst = []
8        res = []
9        # build the graph and track the degree
10        # Time: O(E)
11        for edge in pairs:
12            from_node = edge[0]
13            to_node = edge[1]
14            graph[from_node].append(to_node)
15            indegree[to_node] += 1
16            outdegree[from_node] += 1
17        
18        # find the starting node
19        # time: O(E)
20        start_node = pairs[0][0]
21        for node in outdegree:
22            if outdegree[node]-indegree[node] == 1:
23                start_node = node
24                break
25        
26        # Time: O(E), Space: O(E)
27        def dfs(node):
28            while graph[node]:
29                next_node = graph[node].pop()
30                dfs(next_node)
31            path_lst.append(node)
32        # For Eulerain path, we cannot start at any node
33        # the starting node's outcoming should be 1 more than its incoming
34        # if all nodes' outcoming equals to its incoming, it is a cycle
35        # we can start anywhere if it is a cycle
36        dfs(start_node)
37
38        # Time: O(E)
39        path_lst.reverse()
40        for i in range(len(path_lst)-1):
41            res.append([path_lst[i], path_lst[i+1]])
42        return res   