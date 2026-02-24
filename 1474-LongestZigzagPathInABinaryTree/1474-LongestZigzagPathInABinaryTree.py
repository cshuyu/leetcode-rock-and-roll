# Last updated: 2/23/2026, 6:44:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLength = 0

        def dfs(node, isNextLeft, currLength):
            nonlocal maxLength
            maxLength = max(maxLength, currLength)
            if node.left:
                if isNextLeft:
                    dfs(node.left, False, currLength+1)
                else:
                    dfs(node.left, False, 1)
            if node.right:
                if isNextLeft:
                    dfs(node.right, True, 1)
                else:
                    dfs(node.right, True, currLength+1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return maxLength
