# Last updated: 7/12/2026, 11:17:19 PM
# LinkedList Recursion
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
12        def reverse(head):
13            if not head or not head.next:
14                return head 
15            else:
16                new_head = head.next
17                next_node = new_head.next
18                head.next = reverse(next_node)
19                new_head.next = head
20                return new_head
21        
22        return reverse(head)