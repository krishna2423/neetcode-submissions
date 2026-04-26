# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def interleave(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            l1.next = interleave(l2, l1.next)
            return l1
        
        size = 0 
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        size = (size + 1)// 2

        curr = head
        for _ in range(size - 1):
            curr = curr.next
        
        second = curr.next 
        curr.next = None

        curr = second
        prev = None
        while curr:
            n = curr.next
            curr.next = prev 
            prev = curr
            curr = n 

        interleave(head, prev)
            