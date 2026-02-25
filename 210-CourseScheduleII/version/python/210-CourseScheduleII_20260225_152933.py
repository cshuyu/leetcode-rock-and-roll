# Last updated: 2/25/2026, 3:29:33 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        indegree = [0]*numCourses
4        res = []
5        graph = self.buildGraph(numCourses, prerequisites, indegree)
6        node_queue = deque()
7        for node in range(numCourses):
8            if indegree[node]==0:
9                node_queue.append(node)
10        
11        while node_queue:
12            curr_node = node_queue.popleft()
13            res.append(curr_node)
14            for next_node in graph[curr_node]:
15                indegree[next_node] -= 1
16                if indegree[next_node]==0:
17                    node_queue.append(next_node)
18        
19        if len(res)==numCourses:
20            return res
21        else:
22            return []
23
24    def buildGraph(self, numCourses, prerequisites, indegree):
25        graph = [[] for _ in range(numCourses)]
26        for edge in prerequisites:
27            from_idx = edge[1]
28            to_idx = edge[0]
29            graph[from_idx].append(to_idx)
30            indegree[to_idx] += 1
31        return graph
32        