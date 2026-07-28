# Last updated: 7/27/2026, 5:49:06 PM
# BST: inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        vals = []
10
11        def inorder(node):
12            if not node:
13                return
14            inorder(node.left)
15            vals.append(node.val)
16            inorder(node.right)
17    
18        def build(left, right):
19            if left>right:
20                return None
21            mid = left+(right-left)//2
22            node = TreeNode(vals[mid])
23            node.left = build(left, mid-1)
24            node.right = build(mid+1, right)
25            return node
26    
27        inorder(root)
28        return build(0, len(vals)-1)