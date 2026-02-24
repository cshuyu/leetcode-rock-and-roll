# Last updated: 2/23/2026, 6:46:26 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(node, res):
            if not node:
                return 0
            else:
                left = helper(node.left, res)
                right = helper(node.right, res)
                res[0] = max(res[0], left+right)
                return 1+max(left, right)
        res = [0]
        helper(root, res)
        return res[0]


    


        