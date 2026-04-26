# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """seen = set()

        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        
        return False"""
        
        f = head
        s = head

        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        return False        