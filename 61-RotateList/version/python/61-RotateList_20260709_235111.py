# Last updated: 7/9/2026, 11:51:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k==0:
9            return head
10        end = head
11        length = 0
12        while end is not None:
13            end = end.next
14            length += 1
15        steps = k%length
16        if steps == 0:
17            return head
18
19        def reverse(head):
20            prev = None
21            while head is not None:
22                tmp = head.next
23                head.next = prev
24                prev = head
25                head = tmp
26            return prev
27
28        head = reverse(head)
29        left = right = head
30        for i in range(steps-1):
31            right = right.next
32        next_start = right.next
33        right.next = None
34        newHead = reverse(left)
35        nextHead = reverse(next_start)
36        head.next = nextHead
37        return newHead
38
39