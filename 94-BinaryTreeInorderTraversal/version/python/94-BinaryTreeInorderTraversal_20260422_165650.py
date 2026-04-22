# Last updated: 4/22/2026, 4:56:50 PM
# DFS with InOrder iterative traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        res = []
12        stack = []
13        curr = root
14        while curr or stack:
15            if curr:
16                stack.append(curr)
17                curr = curr.left
18            else:
19                peek = stack.pop()
20                res.append(peek.val)
21                if peek.right:
22                    curr = peek.right
23        return res
24        
25        
26
27        