# Last updated: 2/25/2026, 1:41:15 PM
# Graph: traverse(DFS)
1class Solution:
2    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
3        res = []
4        if not graph:
5            return graph
6        def helper(node, curr_path):
7            if node == len(graph)-1:
8                res.append(list(curr_path))
9                return
10            if not graph[node]:
11                return
12            for next_node in graph[node]:
13                curr_path.append(next_node)
14                helper(next_node, curr_path)
15                curr_path.pop()    
16        helper(0, [0])
17        return res