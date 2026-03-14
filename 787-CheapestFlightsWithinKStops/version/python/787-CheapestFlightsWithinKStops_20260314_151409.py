# Last updated: 3/14/2026, 3:14:09 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        # Bellman-Ford Algorithm, time complexity is O(E*k), space complexity is O(V)
4        prices = [float("inf")]*n
5        prices[src] = 0
6        for i in range(k+1):
7            tmp = prices[:]
8            for u, v, w in flights:
9                if prices[u] == float("inf"):
10                    continue
11                if tmp[v] > w + prices[u]:
12                    tmp[v] = w + prices[u]
13            prices = tmp
14        return prices[dst] if prices[dst]!=float("inf") else -1
15                
16
17    
18
19
20
21
22
23
24