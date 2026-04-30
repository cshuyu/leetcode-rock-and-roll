# Last updated: 4/30/2026, 12:41:34 AM
# BFS with hashing combinations
1'''
2Time Complexity: O(m*n)!*(m*n)
3Space Complexity: O(m*n)!*(m*n)
4'''
5class Solution:
6    def slidingPuzzle(self, board: List[List[int]]) -> int:
7        target = "123450"
8        start_str = ""
9        start_lst = []
10        for row in board:
11            for val in row:
12                start_lst.append(str(val))
13        start_str = "".join(start_lst)
14        dq = deque()
15        dq.append((start_str, 0))
16        visited = set()
17        visited.add(start_str)
18        mapping = self.generateNeighborMapping(board)
19        while dq:
20            curr, moves = dq.popleft()
21            if curr == target:
22                return moves
23            for neighbor in self.getNeighbors(mapping, curr):
24                if neighbor not in visited:
25                    dq.append((neighbor, moves+1))
26                    visited.add(neighbor)
27        return -1
28    
29    def getNeighbors(self, mapping, curr):
30        neighbors = []
31        idx = curr.index('0')
32        for swap_idx in mapping[idx]:
33            neighbor = self.swap(curr, idx, swap_idx)
34            neighbors.append(neighbor)
35        return neighbors
36    
37    def generateNeighborMapping(self, board):
38        m = len(board)
39        n = len(board[0])
40        mapping = defaultdict(list)
41        for i in range(m*n):
42            if i%n != 0:
43                mapping[i].append(i-1)
44            if i%n != n-1:
45                mapping[i].append(i+1)
46            if i-n >= 0:
47                mapping[i].append(i-n)
48            if i+n < m*n:
49                mapping[i].append(i+n)
50        return mapping
51    
52    def swap(self, s, i, j):
53        str_lst = list(s)
54        str_lst[i], str_lst[j] = str_lst[j], str_lst[i]
55        return "".join(str_lst)
56