# Last updated: 4/1/2026, 11:03:11 AM
# Two pointer with LinkedList
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow = head
9        fast = head
10        while fast:
11            if slow.val != fast.val:
12                slow.next = fast
13                slow = slow.next
14            fast = fast.next
15        if slow:
16            slow.next = None
17        return head
18