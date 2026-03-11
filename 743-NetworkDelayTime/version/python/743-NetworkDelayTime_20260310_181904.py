# Last updated: 3/10/2026, 6:19:04 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        # Time Complexity is EO(logE)
4        graph = defaultdict(list)
5        for u, v, w in times:
6            graph[u].append((v, w))
7
8        # Min-heap stores (accumulated_time, current_node)
9        # heapq sorts tuples based on the first elemen by default
10        pq = [(0, k)]
11        shortest_path = {}
12
13        while pq:
14            time, u = heapq.heappop(pq)
15            if u in shortest_path:
16                continue
17            shortest_path[u] = time
18            for v, w in graph[u]:
19                if v not in shortest_path:
20                    heapq.heappush(pq, (time+w, v))
21        
22        if len(shortest_path) == n:
23            return max(shortest_path.values())
24        return -1