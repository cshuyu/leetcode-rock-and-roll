# Last updated: 7/13/2026, 5:44:34 PM
# LinkedList recursion
1"""
2Time: O(n)
3Space: O(n)
4"""
5# Definition for singly-linked list.
6# class ListNode:
7#     def __init__(self, val=0, next=None):
8#         self.val = val
9#         self.next = next
10class Solution:
11    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
12            if not head or not head.next:
13                return head
14            else:
15                new_head = head.next
16                successor = new_head.next
17                new_head.next = head
18                head.next = self. swapPairs(successor)
19                return new_head