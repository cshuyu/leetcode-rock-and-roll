# Last updated: 8/24/2026, 3:26:46 PM
# Tree Isomorphism via Triplet
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
9        trees = {}
10        count = defaultdict(int)
11        res = []
12        def traverse(node):
13            if not node:
14                return 0
15            triplet = (node.val, traverse(node.left), traverse(node.right))
16            if triplet not in trees:
17                trees[triplet] = len(trees)+1
18            tree_id = trees[triplet]
19            
20            count[tree_id] += 1
21            if count[tree_id]==2:
22                res.append(node)
23            return tree_id
24        
25        traverse(root)
26        return res