# Last updated: 2/23/2026, 6:44:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            if node.val >= maxVal:
                goodCnt = 1
                maxVal = node.val
            else:
                goodCnt = 0
            
            leftCnt = dfs(node.left, maxVal)
            rightCnt = dfs(node.right, maxVal)

            return goodCnt + leftCnt + rightCnt
        
        return dfs(root, root.val)