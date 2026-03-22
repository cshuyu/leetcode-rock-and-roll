# Last updated: 3/21/2026, 6:31:21 PM
1class Solution:
2    # we need to use all tickets, therefore it needs to go through all edges
3    # Eulerain Path
4    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
5        graph = defaultdict(list)
6        for u, v in tickets:
7            graph[u].append(v)
8        for node in graph:
9            graph[node].sort(reverse=True)
10
11        path = []
12
13        def dfs(node):
14            while graph[node]:
15                next_node = graph[node].pop()
16                dfs(next_node)
17                path.append(next_node)
18        
19        dfs("JFK")
20        path.append("JFK")
21        
22        return path[::-1] 
23                    
24