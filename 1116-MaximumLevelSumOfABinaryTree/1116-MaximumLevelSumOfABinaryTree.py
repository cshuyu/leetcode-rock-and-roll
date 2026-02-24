# Last updated: 2/23/2026, 6:44:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_queue = deque([root])
        max_sum = root.val
        curr_level = 0
        res = 1
        while node_queue:
            curr_len = len(node_queue)
            curr_level += 1
            curr_sum = 0
            for i in range(0, curr_len):
                curr_node = node_queue.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                res = curr_level
        
        return res
                



