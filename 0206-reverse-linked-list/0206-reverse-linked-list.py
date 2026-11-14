# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head :
            return None 
        prev = None 
        node = head 
        nex = head.next 
        while node :
            nex = node.next 
            node.next = prev
            prev = node 
            node = nex 
        return prev
            

