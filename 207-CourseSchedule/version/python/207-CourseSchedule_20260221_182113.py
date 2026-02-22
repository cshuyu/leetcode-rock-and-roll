# Last updated: 2/21/2026, 6:21:13 PM
# Graph: DFS traverse with onPath
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = self.buildGraph(numCourses, prerequisites)
4        hasCycle = False
5        onPath = [False]*numCourses
6        visited = [False]*numCourses
7
8        def helper(node, visited, onPath):
9            nonlocal hasCycle
10            if hasCycle:
11                return
12            if onPath[node]:
13                hasCycle = True
14                return
15            if visited[node]:
16                return
17            visited[node] = True
18            onPath[node] = True
19            for j in graph[node]:
20                helper(j, visited, onPath)
21            onPath[node] = False
22        
23        for i in range(numCourses):
24            if not visited[i]:
25                helper(i, visited, onPath)
26        return not hasCycle
27
28    def buildGraph(self, numCourses, prerequisites):
29        graph = [[] for _ in range(numCourses)]
30        for edge in prerequisites:
31            from_idx = edge[1]
32            to_idx = edge[0]
33            graph[from_idx].append(to_idx)
34        return graph
35        
36