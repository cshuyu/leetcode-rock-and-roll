# Last updated: 4/22/2026, 6:35:22 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7'''
8Time complexity is O(n)
9Space complexity, worst case the biggest level amount is n/2, so it is also O(n)
10'''
11class Solution:
12    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
13        dq = deque()
14        res = []
15        if not root:
16            return res
17        dq.append(root)
18        while dq:
19            level_len = len(dq)
20            level_nodes = []
21            for i in range(level_len):
22                curr = dq.popleft()
23                level_nodes.append(curr.val)
24                if curr.left:
25                    dq.append(curr.left)
26                if curr.right:
27                    dq.append(curr.right)
28            res.append(level_nodes)
29        return res
30        