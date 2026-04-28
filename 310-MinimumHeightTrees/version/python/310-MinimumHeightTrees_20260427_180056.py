# Last updated: 4/27/2026, 6:00:56 PM
# BFS for tree's topologic traverse
1'''
2Time Complexity：O(n)
3Space Complexity：O(n)
4'''
5class Solution:
6    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
7        if n<=2:
8            return [i for i in range(n)]
9        connection = defaultdict(list)
10        degree = defaultdict(int)
11        for i in range(len(edges)):
12            u, v = edges[i]
13            connection[u].append(v)
14            connection[v].append(u)
15            degree[u] += 1
16            degree[v] += 1
17        
18        queue = deque()
19        for key in degree:
20            if degree[key]==1:
21                queue.append(key)
22        
23        res = []
24        remain_nodes = n
25        while remain_nodes>2:
26            level_len = len(queue)
27            remain_nodes -= level_len
28            for i in range(level_len):
29                curr_node = queue.popleft()
30                for next_node in connection[curr_node]:
31                    degree[next_node] -= 1
32                    if degree[next_node]==1:
33                        queue.append(next_node)
34                 
35        return list(queue)