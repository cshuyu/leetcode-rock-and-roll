# Last updated: 7/7/2026, 4:33:26 PM
# LinkedList: Two pointers
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7O(Time): O(max(m, n))
8O(Space): O(max(m, n))
9"""
10class Solution:
11    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
12        dummy = ListNode(-1)
13        p = dummy
14        p1 = l1
15        p2 = l2
16
17        while p1 is not None or p2 is not None:
18            curr_sum = 0
19            if p.next is None:
20                p.next = ListNode(0)
21            else:
22                curr_sum = p.next.val
23            if p1 is not None:
24                curr_sum += p1.val
25                p1 = p1.next
26            if p2 is not None:
27                curr_sum += p2.val
28                p2 = p2.next
29            p.next.val = curr_sum%10
30            p = p.next
31            if curr_sum>=10:
32                p.next = ListNode(int(curr_sum/10))
33        
34        return dummy.next
35