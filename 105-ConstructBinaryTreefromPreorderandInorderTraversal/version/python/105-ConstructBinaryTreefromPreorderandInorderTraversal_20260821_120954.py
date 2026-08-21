# Last updated: 8/21/2026, 12:09:54 PM
# Binary Tree Build: recuirsion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9Space: O(n)
10"""
11class Solution:
12    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
13        value_idx_dict = {}
14        for i in range(len(inorder)):
15            value_idx_dict[inorder[i]] = i
16        def buildHelper(preorder_start, preorder_end, inorder_start, inorder_end):
17            if preorder_start > preorder_end:
18                return None
19            root_val = preorder[preorder_start]
20            if root_val in value_idx_dict:
21                index = value_idx_dict[root_val]
22            else:
23                print(f"no value {root_val} in the inorder list")
24            root = TreeNode(root_val)
25            left_size = index-inorder_start
26            root.left = buildHelper(preorder_start+1, preorder_start+left_size, inorder_start, index-1)
27            root.right = buildHelper(preorder_start+left_size+1, preorder_end, index+1, inorder_end)
28            return root
29        return buildHelper(0, len(preorder)-1, 0, len(inorder)-1)
30
31