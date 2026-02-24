# Last updated: 2/23/2026, 6:45:19 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        def helper(node):
            if node is None:
                return node
            res.append(node.val)
            for child in node.children:
                helper(child)
        
        helper(root)       
        return res