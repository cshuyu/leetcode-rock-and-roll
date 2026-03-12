# Last updated: 3/11/2026, 6:14:49 PM
# Shortes path with Constraints: Bellman-Ford algorithm
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        '''
4        The Bellman-Ford method time complexity is k*O(E), the space complexity is O(V)
5        The Dijkstra method time complexity is E*logO(E), the sapce complexity is O(V+E)
6        Choosing Bellman-Ford method or Dijkstra depend on if K is approaching to V, if K<O(logE)
7        '''
8        # Step1: Initialize distance with infinity
9        prices = [float("inf")] * n
10        prices[src] = 0
11
12        # Step2: Interate K+1 times 
13        # each iteration represents one more allowed jump
14        for i in range(k+1):
15            # [:] is a shallow copy, we change one won't affect another
16            tmp_prices = prices[:]
17            for u, v, w in flights:
18                if prices[u] == float('inf'):
19                    continue
20                if prices[u] + w < tmp_prices[v]:
21                    tmp_prices[v] = prices[u]+w
22            prices = tmp_prices
23
24        return prices[dst] if prices[dst] != float('inf') else -1
25                
26