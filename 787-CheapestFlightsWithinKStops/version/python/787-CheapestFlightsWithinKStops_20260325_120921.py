# Last updated: 3/25/2026, 12:09:21 PM
# Graph: Dijkstra with K stops constraints
1# Space Complexity: 
2# Time Complexity: 
3class Solution:
4    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
5        '''
6        Time Complexity:
7        1) graph_build: O(V+E)
8        2) heap pop: E*K*O(logEK)
9        3) heap push: E*K*O(logEK)
10
11        Space Complexity:
12        1) graph: O(V+E)
13        2) min_stop: O(V)
14        3) heap: O(EK)
15        '''
16        graph = defaultdict(list)
17        for u, v, w in flights:
18            graph[u].append((v, w))
19        min_stop = [float("inf")] * n
20        # weight, node, stop
21        pq =[(0, src, 0)]
22        while pq:
23            cost, curr_node, stop = heapq.heappop(pq)
24            if curr_node == dst:
25                return cost
26            if stop>k:
27                continue
28            if stop < min_stop[curr_node]:
29                min_stop[curr_node] = stop
30                # pay attent the for loop needs to inside the prune if condition
31                for next_node, weight in graph[curr_node]:
32                    heapq.heappush(pq, (cost+weight, next_node, stop+1))
33        
34        return -1
35