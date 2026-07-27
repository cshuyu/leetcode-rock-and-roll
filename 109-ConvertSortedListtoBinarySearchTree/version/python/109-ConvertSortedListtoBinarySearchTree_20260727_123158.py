# Last updated: 7/27/2026, 12:31:58 PM
# BST: Inorder traverse
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6# Definition for a binary tree node.
7# class TreeNode:
8#     def __init__(self, val=0, left=None, right=None):
9#         self.val = val
10#         self.left = left
11#         self.right = right
12class Solution:
13    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
14        if not head:
15            return head
16        def get_size(node):
17            size = 0
18            while node:
19                size += 1
20                node = node.next
21            return size
22        size = get_size(head)
23
24        def inorder(left, right):
25            nonlocal head
26            if left > right:
27                return None
28            mid = left + (right-left)//2
29            left_node = inorder(left, mid-1)
30            root = TreeNode(head.val)
31            root.left = left_node
32            head = head.next
33            right_node = inorder(mid+1, right)
34            root.right = right_node
35            return root
36        
37        return inorder(0, size-1)
38