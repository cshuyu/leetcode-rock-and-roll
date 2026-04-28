# Last updated: 4/28/2026, 11:31:40 AM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited = set()
4        stack = []
5        stack.append(0)
6        while stack:
7            curr_node = stack.pop()
8            visited.add(curr_node)
9            for next_node in rooms[curr_node]:
10                if next_node not in visited:
11                    stack.append(next_node)
12        if len(visited)==len(rooms):
13            return True
14        else:
15            return False
16
17
18
19
20