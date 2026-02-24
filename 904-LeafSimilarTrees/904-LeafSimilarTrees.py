# Last updated: 2/23/2026, 6:45:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root: TreeNode):
            lst = []
            if root:
                if not root.left and not root.right:
                    lst.append(root.val)
                else:
                    lst = helper(root.left) + helper(root.right)
            return lst

        return helper(root1) == helper(root2)
            


        