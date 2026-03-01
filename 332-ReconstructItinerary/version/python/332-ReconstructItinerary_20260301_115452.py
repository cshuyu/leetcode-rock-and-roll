# Last updated: 3/1/2026, 11:54:52 AM
# Graph: Eulerian Path Traverse(DFS post order)
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        # 1. Build the graph
4        graph = defaultdict(list)
5        
6        # TRICK 1: Sort the tickets in REVERSE alphabetical order before building the graph.
7        # This allows us to use .pop() to get the alphabetically smallest destination in O(1) time!
8        tickets.sort(reverse=True)
9        for src, dst in tickets:
10            graph[src].append(dst)
11            
12        itinerary = []
13        
14        # 2. Define Hierholzer's DFS
15        def dfs(airport):
16            # While there are still outgoing flights from this airport
17            while graph[airport]:
18                # Pop the alphabetically smallest destination
19                next_dest = graph[airport].pop()
20                dfs(next_dest)
21                
22            # TRICK 2: We only add the airport to the itinerary AFTER 
23            # all its outgoing edges have been explored (we hit a dead end).
24            itinerary.append(airport)
25            
26        # 3. Start the journey
27        dfs("JFK")
28        
29        # 4. The itinerary was built backwards from the dead ends, so reverse it!
30        return itinerary[::-1]
31