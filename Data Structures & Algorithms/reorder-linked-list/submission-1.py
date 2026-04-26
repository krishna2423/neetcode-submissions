# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def interleave(l1, l2):
            while l1 and l2:
                n1, n2 = l1.next, l2.next
                l1.next = l2
                l2.next = n1
                l1, l2 = n1, n2
        
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
            