# Last updated: 10/23/2026, 11:55:53 PM
# BST: recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8'''
9O(Time): O(logn)
10O(Space): O(logn)
11'''
12class Solution:
13    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
14        if not nums:
15            return None
16
17        def helper(i, j):
18            if i>j:
19                return None
20            mid = i+(j-i)//2
21            val = nums[mid]
22            root = TreeNode(val)
23            root.left = helper(i, mid-1)
24            root.right = helper(mid+1, j)
25            return root
26        
27        return helper(0, len(nums)-1)
28    