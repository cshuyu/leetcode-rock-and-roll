# Last updated: 3/3/2026, 11:53:02 AM
# Graph: Bipartite(BFS+mutual dislike)
1class Solution:
2    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
3        color = [0]*(n+1)
4        queue = deque()
5        graph = defaultdict(list)
6        # Dislike is mutual dislike for Bipartition
7        for edge in dislikes:
8            graph[edge[0]].append(edge[1])
9            graph[edge[1]].append(edge[0])
10        
11        for node in range(1, n+1):
12            if color[node] == 0:
13                color[node] = 1
14                queue.append(node)
15            while queue:
16                curr_node = queue.popleft()
17                for next_node in graph[curr_node]:
18                    if color[next_node] == 0:
19                        color[next_node] = -1 * color[curr_node]
20                        queue.append(next_node)
21                    elif color[next_node] != -1 * color[curr_node]:
22                        return False
23
24        return True
25
26
27
28
29