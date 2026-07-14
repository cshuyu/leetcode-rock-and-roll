# Last updated: 7/13/2026, 5:00:24 PM
# LinkedList: recursion
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7Time: O(n)
8Space: O(k+n/k), worst case, if k==1, it is O(n)
9"""
10class Solution:
11    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
12        curr = head
13        for i in range(k):
14            if curr is None:
15                return head
16            else:
17                curr = curr.next
18        
19        # guarantee head is not None
20        def reverseN(head, n):
21            if n==1:
22                return head, head.next
23            else:
24                new_head, successor = reverseN(head.next, n-1)
25                if new_head == head:
26                    return head
27                head.next.next = head
28                head.next = successor
29                return new_head, successor
30        
31        new_head, successor = reverseN(head, k)
32        head.next = self.reverseKGroup(successor, k)
33        return new_head
34