# Last updated: 7/27/2026, 1:27:44 PM
1"""
2Use of inorder traverse to move the head to the mid.
3By this way, it reduce the O(time) from O(nlogn) to O(n)
4but it needs the O(space) as O(n)
5"""
6# Definition for singly-linked list.
7# class ListNode:
8#     def __init__(self, val=0, next=None):
9#         self.val = val
10#         self.next = next
11# Definition for a binary tree node.
12# class TreeNode:
13#     def __init__(self, val=0, left=None, right=None):
14#         self.val = val
15#         self.left = left
16#         self.right = right
17class Solution:
18    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
19        if not head:
20            return head
21        def get_size(node):
22            size = 0
23            while node:
24                size += 1
25                node = node.next
26            return size
27        size = get_size(head)
28
29        def inorder(left, right):
30            nonlocal head
31            if left > right:
32                return None
33            mid = left + (right-left)//2
34            left_node = inorder(left, mid-1)
35            root = TreeNode(head.val)
36            root.left = left_node
37            head = head.next
38            right_node = inorder(mid+1, right)
39            root.right = right_node
40            return root
41        
42        return inorder(0, size-1)
43