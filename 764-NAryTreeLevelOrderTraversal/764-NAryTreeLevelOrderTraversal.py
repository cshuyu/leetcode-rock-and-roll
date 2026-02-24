# Last updated: 2/23/2026, 6:45:21 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        res = []
        q = deque()
        q.append(root)
        while q:
            level_count = len(q)
            level = []
            while level_count>0:
                curr = q.popleft()
                level_count -= 1
                level.append(curr.val)
                for child in curr.children:
                    q.append(child)
            res.append(level)
        return res
                


        