# Last updated: 7/13/2026, 10:34:18 AM
# LinkedList_reverse
1"""
2Iterative way: Cut and Connect Framework
3Time: O(n)
4Space:O(n)
5"""
6# Definition for singly-linked list.
7# class ListNode:
8#     def __init__(self, val=0, next=None):
9#         self.val = val
10#         self.next = next
11class Solution:
12    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
13
14        def reverseN(head, n):
15            if n==1 or not head.next:
16                return head, head.next
17            else:
18                tail, successor = reverseN(head.next, n-1)
19                head.next.next = head
20                head.next = successor
21            return tail, successor
22
23        if left==1:
24            new_head, _ = reverseN(head, right)
25            return new_head
26        else:
27            head.next = self.reverseBetween(head.next, left-1, right-1)
28        return head
29        