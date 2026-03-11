# Last updated: 3/11/2026, 11:59:11 AM
# Shortest Path with weight: Dijstra(BFS+heap)
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        # Time Complexity is graph_build_time+heap_through_time
4        # graph_build_time is O(V+E), 
5        # every heap_push or heap_pop is O(logE), heap_through_time is E*O(logE)
6        # Total time is E*log(E)
7        # Space Complexity is graph_space+heap_space+shortest_path
8        # graph_space is O(V+E)+O(E)+O(V), total is O(V+E)
9        graph = defaultdict(list)
10        for u, v, w in times:
11            graph[u].append((v, w))
12
13        # Min-heap stores (accumulated_time, current_node)
14        # heapq sorts tuples based on the first elemen by default
15        pq = [(0, k)]
16        shortest_path = {}
17
18        while pq:
19            time, u = heapq.heappop(pq)
20            if u in shortest_path:
21                continue
22            shortest_path[u] = time
23            for v, w in graph[u]:
24                if v not in shortest_path:
25                    heapq.heappush(pq, (time+w, v))
26        
27        if len(shortest_path) == n:
28            return max(shortest_path.values())
29        return -1