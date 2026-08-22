# Last updated: 8/22/2026, 3:38:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7Time: O(n)
8Space: O(n)
9class Solution:
10    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
11        val_idx_dict = {}
12        for i in range(len(inorder)):
13            val_idx_dict[inorder[i]] = i
14
15        def build(inorder_start, inorder_end, postorder_start, postorder_end):
16            if postorder_start>postorder_end or inorder_start>inorder_end:
17                return None
18            root_val = postorder[postorder_end]
19            root = TreeNode(root_val)
20            idx = val_idx_dict[root_val]
21            right_size = inorder_end-idx
22            root.left = build(inorder_start, idx-1, postorder_start, postorder_end-right_size-1)
23            root.right = build(idx+1, inorder_end, postorder_end-right_size, postorder_end-1)
24            return root
25        
26        return build(0, len(inorder)-1, 0, len(postorder)-1)