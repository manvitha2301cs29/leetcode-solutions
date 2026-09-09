# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head
        h = head
        c = 1 
        while h.next:
            h = h.next
            c += 1
        h.next = head
        s = head 
        x = c - k%c
        p = s
        while x :
            p =  s
            s = s.next
            x -= 1
        p.next = None 
        return s 