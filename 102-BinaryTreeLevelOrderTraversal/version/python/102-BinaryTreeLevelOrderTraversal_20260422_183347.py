# Last updated: 4/22/2026, 6:33:47 PM
# BFS with level traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        dq = deque()
10        res = []
11        if not root:
12            return res
13        dq.append(root)
14        while dq:
15            level_len = len(dq)
16            level_nodes = []
17            for i in range(level_len):
18                curr = dq.popleft()
19                level_nodes.append(curr.val)
20                if curr.left:
21                    dq.append(curr.left)
22                if curr.right:
23                    dq.append(curr.right)
24            res.append(level_nodes)
25        return res
26        