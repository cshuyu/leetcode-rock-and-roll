# Last updated: 2/24/2026, 11:01:25 AM
# Graph: topological sort(DFS)
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = self.buildGraph(numCourses, prerequisites)
4        visited = [False]*numCourses
5        onPath = [False]*numCourses
6
7        def hasCycle(node):
8            if onPath[node]:
9                return True
10            if visited[node]:
11                return False
12            visited[node] = True
13            onPath[node] = True
14            for next_node in graph[node]:
15                if hasCycle(next_node):
16                    return True
17            onPath[node] = False
18            return False
19
20        for from_node in range(numCourses):
21            if not visited[from_node]:
22                if hasCycle(from_node):
23                    return False
24        return True
25
26    def buildGraph(self, numCourses, prerequisites):
27        graph = [[] for _ in range(numCourses)]
28        for edge in prerequisites:
29            from_idx = edge[1]
30            to_idx = edge[0]
31            graph[from_idx].append(to_idx)
32        return graph 