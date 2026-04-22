# Last updated: 4/22/2026, 12:58:49 PM
# DFS with PostOrder iterative traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        stack = []
12        res = []
13        curr = root
14        last_visited = None
15        while curr or stack:
16            if curr:
17                stack.append(curr)
18                curr = curr.left
19            else:
20                peek = stack[-1]
21                if peek.right and last_visited != peek.right:
22                    curr = peek.right
23                else:
24                    res.append(peek.val)
25                    last_visited = stack.pop()
26        return res
27