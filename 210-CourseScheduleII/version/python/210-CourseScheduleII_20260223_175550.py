# Last updated: 2/23/2026, 5:55:50 PM
# Graph: topological sort_BFS
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        indegree = [0]*numCourses
4        graph = self.buildGraph(numCourses, prerequisites, indegree)
5        queue = deque()
6        res = []
7        for from_idx in range(numCourses):
8            count = indegree[from_idx]
9            if count == 0:
10                queue.append(from_idx)
11        while queue:
12            curr_node = queue.popleft()
13            res.append(curr_node)
14            for next_node in graph[curr_node]:
15                indegree[next_node] -= 1
16                if indegree[next_node] == 0:
17                    queue.append(next_node)
18        if len(res) != numCourses:
19            return []
20        return res
21
22    def buildGraph(self, numCourses, prerequisites, indegree):
23        graph = [[] for _ in range(numCourses)]
24        for edge in prerequisites:
25            from_idx = edge[1]
26            to_idx = edge[0]
27            graph[from_idx].append(to_idx)
28            indegree[to_idx] += 1
29        return graph
30