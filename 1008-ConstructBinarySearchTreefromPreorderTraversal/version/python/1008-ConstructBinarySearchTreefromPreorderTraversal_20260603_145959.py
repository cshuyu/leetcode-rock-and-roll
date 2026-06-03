# Last updated: 6/3/2026, 2:59:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
9        def build(preorder, start, end):
10            if start > end:
11                return None
12            rootVal = preorder[start]
13            root = TreeNode(rootVal)
14            p = start+1
15            while p<=end:
16                if preorder[p]<rootVal:
17                    p += 1
18                else:
19                    break
20            root.left = build(preorder, start+1, p-1)
21            root.right = build(preorder, p, end)
22            return root
23
24        return build(preorder, 0, len(preorder)-1)