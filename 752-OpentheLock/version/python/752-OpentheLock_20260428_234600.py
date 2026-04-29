# Last updated: 4/28/2026, 11:46:00 PM
# BFS with Graph Traverse
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        if target == "0000":
4            return 0
5        dead = set(deadends)
6        if "0000" in dead:
7            return -1
8        dq = deque()
9        dq.append(("0000", 0))
10        visited = set("0000")
11        while dq:
12            curr, moves = dq.popleft()
13            for i in range(len(curr)):
14                for change in [-1, 1]:
15                    change_c = (int(curr[i])+change)%10
16                    next = curr[:i]+str(change_c)+curr[i+1:]
17                    if next == target:
18                        return moves+1
19                    if next not in dead and next not in visited:
20                        dq.append((next, moves+1))
21                        visited.add(next)
22        return -1
23
24
25
26