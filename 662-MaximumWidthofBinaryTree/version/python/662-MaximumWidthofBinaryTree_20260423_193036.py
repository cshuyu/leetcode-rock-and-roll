# Last updated: 4/23/2026, 7:30:36 PM
# BFS with level index
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        dq = deque()
10        dq.append((root, 0))
11        max_len = 0
12        while dq:
13            level_len = len(dq)
14            _, first_idx = dq[0]
15            for i in range(level_len):
16                curr_node, curr_idx = dq.popleft()
17                if curr_node.left:
18                    dq.append((curr_node.left, 2*curr_idx))
19                if curr_node.right:
20                    dq.append((curr_node.right, 2*curr_idx+1))
21            max_len = max(max_len, curr_idx-first_idx+1)
22        return max_len
23            
24
25
26