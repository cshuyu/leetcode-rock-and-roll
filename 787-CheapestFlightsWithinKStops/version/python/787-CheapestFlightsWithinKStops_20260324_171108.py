# Last updated: 3/24/2026, 5:11:08 PM
1# Space Complexity: 
2# Time Complexity: 
3class Solution:
4    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
5        graph = defaultdict(list)
6        for u, v, w in flights:
7            graph[u].append((v, w))
8        min_stop = [float("inf")] * n
9        # weight, node, stop
10        pq =[(0, src, 0)]
11        while pq:
12            cost, curr_node, stop = heapq.heappop(pq)
13            if curr_node == dst:
14                return cost
15            if stop>k:
16                continue
17            if stop < min_stop[curr_node]:
18                min_stop[curr_node] = stop
19                # pay attent the for loop needs to inside the prune if condition
20                for next_node, weight in graph[curr_node]:
21                    heapq.heappush(pq, (cost+weight, next_node, stop+1))
22        
23        return -1
24