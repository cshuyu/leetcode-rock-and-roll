# Last updated: 3/11/2026, 4:31:25 PM
# Shortest Path with Constraints: Dijkstra with Prune
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        graph = defaultdict(list)
4        for u, v, w in flights:
5            graph[u].append([v, w])
6        # the min_heap is (weight, current_stops, node)
7        min_heap = [(0, 0, src)]
8        # Track the min stops it took to reach a node
9        # If we reach a node again but with more stops, it's a worse path.
10        visited_stops = [float('inf')] * n
11
12        while min_heap:
13            weight, stops, curr_node = heapq.heappop(min_heap)
14            if curr_node == dst:
15                return weight
16            # If we aren't at 'dst', and stops > k, 
17            # this path has used all allowed stpes, it is dead.
18            if stops > k:
19                continue
20            # prune: if we've reached this node before with fewer stops, 
21            # don't explore this path.
22            if stops >= visited_stops[curr_node]:
23                continue
24            visited_stops[curr_node] = stops
25            for next_node, curr_weight in graph[curr_node]:
26                new_weight = weight + curr_weight
27                heapq.heappush(min_heap, (new_weight, stops+1, next_node))
28        
29        return -1