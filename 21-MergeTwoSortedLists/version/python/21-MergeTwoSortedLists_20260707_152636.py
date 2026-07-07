# Last updated: 7/7/2026, 3:26:36 PM
# LinkedList(Two Pointers)
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6Time: O(max(m, n))
7Space: O(max(m, n))
8class Solution:
9    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
10        dummy = ListNode(-1)
11        p = dummy
12        p1 = list1
13        p2 = list2
14
15        while p1 is not None and p2 is not None:
16            if p1.val > p2.val:
17                p.next = p2
18                p2 = p2.next
19            else:
20                p.next = p1
21                p1 = p1.next
22            p = p.next
23        if p1 is not None:
24            p.next = p1
25        if p2 is not None:
26            p.next = p2
27
28        return dummy.next