# Last updated: 8/23/2026, 3:18:39 PM
# Tree_serialization: postorder
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
9        serialize_count = defaultdict(int)
10        res = []
11        def serialize(node):
12            if not node:
13                return "#"
14            left = serialize(node.left)
15            right = serialize(node.right)
16            sub_tree = f"{left},{right},{node.val}"
17            
18            serialize_count[sub_tree] += 1
19            if serialize_count[sub_tree]==2:
20                res.append(node)
21            return sub_tree
22        serialize(root)
23        return res
24