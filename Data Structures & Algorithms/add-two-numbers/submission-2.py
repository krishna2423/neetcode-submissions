# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        p = res
        while l1 and l2:
            d = l1.val + l2.val + carry
            if d > 9:
                d = d % 10
                carry = 1
            else:
                carry = 0
            
            p.next = ListNode(d)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            d = l1.val + carry
            if d > 9:
                d = d % 10
                carry = 1
            else:
                carry = 0
            p.next = ListNode(d)
            p = p.next
            l1 = l1.next
        while l2:
            d = l2.val + carry
            if d > 9:
                d = d % 10
                carry = 1
            else:
                carry = 0
            p.next = ListNode(d)
            p = p.next
            l2 = l2.next
        if carry == 1:
            p.next = ListNode(1)
            p = p.next
        return res.next