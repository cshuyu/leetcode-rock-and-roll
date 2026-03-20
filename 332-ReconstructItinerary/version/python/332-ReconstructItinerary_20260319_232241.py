# Last updated: 3/19/2026, 11:22:41 PM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        graph = defaultdict(list)
4        # Complexity: O(ElogE)
5        tickets.sort(reverse=True)
6        # Complexity: O(E), space: O(E)
7        for edge in tickets:
8            graph[edge[0]].append(edge[1])
9        res = []
10
11        def dfs(airport):
12            while graph[airport]:
13                next_dest = graph[airport].pop()
14                dfs(next_dest)
15                res.append(next_dest)
16        # Complexity: O(E), space: O(E)
17        dfs("JFK")
18        res.append("JFK")
19
20        return res[::-1]
21