# Last updated: 4/23/2026, 5:05:44 PM
# BFS with level traverse
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution:
12    def connect(self, root: 'Node') -> 'Node':
13        if not root:
14            return root
15        root.next = None
16        dq = deque()
17        dq.append(root)
18        while dq:
19            level_len = len(dq)
20            prev = None
21            for i in range(level_len):
22                curr = dq.popleft()
23                if prev:
24                    prev.next = curr
25                prev = curr
26                if curr.left:
27                    dq.append(curr.left)
28                if curr.right:
29                    dq.append(curr.right)
30        return root
31 