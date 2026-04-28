# Last updated: 4/28/2026, 10:14:31 AM
# BFS transfer to graph
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        dq = deque()
4        dq.append(0)
5        visited = set()
6        while dq:
7            curr_node = dq.popleft()
8            visited.add(curr_node)
9            for next_node in rooms[curr_node]:
10                if next_node in visited:
11                    continue
12                dq.append(next_node)
13        if len(visited)==len(rooms):
14            return True
15        else:
16            return False