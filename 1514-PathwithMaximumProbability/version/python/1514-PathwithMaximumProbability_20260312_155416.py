# Last updated: 3/12/2026, 3:54:16 PM
1class Solution:
2    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
3        graph = defaultdict(list)
4        for i in range(len(edges)):
5            u = edges[i][0]
6            v = edges[i][1]
7            prob = succProb[i]
8            if prob != 0:
9                graph[u].append([-math.log(prob), v])
10                graph[v].append([-math.log(prob), u])
11        
12        min_heap = [(0.0, start_node)]
13        min_costs = {start_node: 0.0}
14
15        while min_heap:
16            curr_prob, curr_node = heapq.heappop(min_heap)
17            if curr_node == end_node:
18                return math.exp(-curr_prob)
19            if curr_prob > min_costs.get(curr_node, float("inf")):
20                continue
21            for prob, next_node in graph[curr_node]:
22                next_prob = curr_prob+prob
23                if next_prob < min_costs.get(next_node, float("inf")):
24                    min_costs[next_node] = next_prob
25                    heapq.heappush(min_heap, (next_prob, next_node))
26        return 0.0
27