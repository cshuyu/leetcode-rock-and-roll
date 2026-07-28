# Last updated: 7/27/2026, 6:43:45 PM
# BST: inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
9        if not nums or len(nums)==0:
10            return None
11
12        def helper(left, right):
13            if left> right:
14                return None
15            mid = (left+right)//2
16            root = TreeNode(nums[mid])
17            root.left = helper(left, mid-1)
18            root.right = helper(mid+1, right)
19            return root
20
21        return helper(0, len(nums)-1)