# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = n
        prev = None
        curr = head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n 
        
        reversed_ll = prev
        steps = k - 2

        if steps < -1:
            return None
        if steps == -1:
            reversed_ll = reversed_ll.next
            prev = None
            curr = reversed_ll 
            while curr:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n 
            return prev
        else:
            curr = reversed_ll
            for _ in range(steps):
                curr = curr.next
            curr.next = curr.next.next
            prev = None
            curr = reversed_ll 
            while curr:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n 
            return prev

