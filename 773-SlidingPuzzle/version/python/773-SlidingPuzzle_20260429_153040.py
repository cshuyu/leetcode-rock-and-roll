# Last updated: 4/29/2026, 3:30:40 PM
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
18        while dq:
19            curr, moves = dq.popleft()
20            if curr == target:
21                return moves
22            for neighbor in self.getNeighbors(board, curr):
23                if neighbor not in visited:
24                    dq.append((neighbor, moves+1))
25                    visited.add(neighbor)
26        return -1
27    
28    def getNeighbors(self, board, curr):
29        neighbors = []
30        mapping = self.generateNeighborMapping(board)
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