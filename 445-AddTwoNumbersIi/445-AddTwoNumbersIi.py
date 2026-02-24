# Last updated: 2/23/2026, 6:47:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbersI(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        rs = dummy_head
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            rs.next = ListNode()
            rs = rs.next
            rs.val = val % 10
            carry = val // 10
            l1 = l1.next
            l2 = l2.next
        
        remaining = l1 if l1 else l2
        while remaining:
            val = remaining.val + carry
            rs.next = ListNode()
            rs = rs.next
            rs.val = val % 10
            carry = val // 10
            remaining = remaining.next

        if carry:
            rs.next = ListNode(val=carry)
        
        return dummy_head.next
    
    def reverseList(self, lst: ListNode) -> ListNode:
        nxt = lst.next
        lst.next = None
        while nxt:
            tmp = nxt.next
            nxt.next = lst
            lst = nxt
            nxt = tmp
        return lst

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1:
            l1 = self.reverseList(l1)
        if l2:
            l2 = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbersI(l1,l2))