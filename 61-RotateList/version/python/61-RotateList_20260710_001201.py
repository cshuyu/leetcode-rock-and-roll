# Last updated: 7/10/2026, 12:12:01 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k==0:
9            return head
10        
11        tail = head
12        length = 0
13        while tail.next:
14            tail = tail.next
15            length += 1
16        length += 1
17        k = k%length
18
19        tail.next = head
20        for i in range(length-k-1):
21            head = head.next
22
23        new_head = head.next
24        head.next = None
25        return new_head
26
27