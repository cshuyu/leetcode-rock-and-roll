# Last updated: 7/13/2026, 10:02:07 PM
# LinkedList: Palindrome
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7Time: O(n)
8Space: O(1)
9"""
10class Solution:
11    def isPalindrome(self, head: Optional[ListNode]) -> bool:
12        if not head or not head.next:
13            return True
14
15        slow = fast = head
16        while fast and fast.next:
17            slow = slow.next
18            fast = fast.next.next
19
20        def reverse(node):
21            prev = None
22            
23            while node is not None:
24                next = node.next
25                node.next = prev
26                prev = node
27                node = next
28            
29            return prev
30
31        left = head
32        right = reverse(slow)
33        while left and right:
34            if left.val != right.val:
35                return False
36            left = left.next
37            right = right.next
38        return True 