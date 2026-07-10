# Last updated: 7/10/2026, 12:14:43 AM
# LinkedList
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7O(Time): O(n)
8O(Space): O(1)
9"""
10class Solution:
11    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
12        if not head or not head.next or k==0:
13            return head
14        
15        tail = head
16        length = 0
17        while tail.next:
18            tail = tail.next
19            length += 1
20        length += 1
21        k = k%length
22
23        tail.next = head
24        for i in range(length-k-1):
25            head = head.next
26
27        new_head = head.next
28        head.next = None
29        return new_head
30
31