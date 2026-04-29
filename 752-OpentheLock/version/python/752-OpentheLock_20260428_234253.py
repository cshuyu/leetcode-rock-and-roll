# Last updated: 4/28/2026, 11:42:53 PM
# BFS with Graph traverse
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        if target == "0000":
4            return 0
5        if "0000" in deadends:
6            return -1
7        dq = deque()
8        dq.append(("0000", 0))
9        visited = set("0000")
10        while dq:
11            curr, moves = dq.popleft()
12            for i in range(len(curr)):
13                for change in [-1, 1]:
14                    change_c = (int(curr[i])+change)%10
15                    next = curr[:i]+str(change_c)+curr[i+1:]
16                    if next == target:
17                        return moves+1
18                    if next not in deadends and next not in visited:
19                        dq.append((next, moves+1))
20                        visited.add(next)
21        return -1
22
23
24
25