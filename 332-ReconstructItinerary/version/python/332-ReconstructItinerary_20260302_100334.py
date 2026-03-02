# Last updated: 3/2/2026, 10:03:34 AM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        graph = defaultdict(list)
4        tickets.sort(reverse=True)
5        for edge in tickets:
6            graph[edge[0]].append(edge[1])
7        res = []
8
9        def dfs(airport):
10            while graph[airport]:
11                next_dest = graph[airport].pop()
12                dfs(next_dest)
13            res.append(airport)
14        
15        dfs("JFK")
16
17        return res[::-1]
18        
19
20
21