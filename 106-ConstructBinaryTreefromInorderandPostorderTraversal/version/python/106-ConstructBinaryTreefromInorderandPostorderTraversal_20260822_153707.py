# Last updated: 8/22/2026, 3:37:07 PM
# Build_binary_tree: recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        val_idx_dict = {}
10        for i in range(len(inorder)):
11            val_idx_dict[inorder[i]] = i
12
13        def build(inorder_start, inorder_end, postorder_start, postorder_end):
14            if postorder_start>postorder_end or inorder_start>inorder_end:
15                return None
16            root_val = postorder[postorder_end]
17            root = TreeNode(root_val)
18            idx = val_idx_dict[root_val]
19            right_size = inorder_end-idx
20            root.left = build(inorder_start, idx-1, postorder_start, postorder_end-right_size-1)
21            root.right = build(idx+1, inorder_end, postorder_end-right_size, postorder_end-1)
22            return root
23        
24        return build(0, len(inorder)-1, 0, len(postorder)-1)