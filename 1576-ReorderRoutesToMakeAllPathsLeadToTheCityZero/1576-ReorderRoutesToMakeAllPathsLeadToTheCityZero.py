# Last updated: 2/23/2026, 6:44:34 PM
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append([v, 1])
            adj[v].append([u, 0])
        count = 0
        visited = [False]*n
        visited[0] = True

        def dfs(curr_node):
            nonlocal count
            for neighbor, cost in adj[curr_node]:
                if not visited[neighbor]:
                    count += cost
                    visited[neighbor] = True
                    dfs(neighbor)              
        
        dfs(0)
        return count


        