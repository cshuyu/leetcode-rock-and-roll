# Last updated: 4/24/2026, 3:27:48 PM
# BFS level traverse for completeness tree
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
9        if not root:
10            return True
11        dq = deque()
12        dq.append(root)
13        no_child = False
14        while dq:
15            curr = dq.popleft()
16            if curr.left:
17                if no_child:
18                    return False
19                dq.append(curr.left)
20            else:
21                no_child = True
22            if curr.right:
23                if no_child:
24                    return False
25                dq.append(curr.right)
26            else:
27                no_child = True
28        return True
29