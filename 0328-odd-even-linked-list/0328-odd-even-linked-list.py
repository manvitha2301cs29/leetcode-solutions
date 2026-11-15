# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head :
            return None 
        if not head.next :
            return head
        o = head 
        e = head.next
        oe  = head.next
        while e and  e.next :
            
            o.next = e.next 
            
            e.next = e.next.next
            o = o.next 
            e = e.next 
        o.next = oe 
        return head 
