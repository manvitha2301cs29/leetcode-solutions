# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dum = ListNode(0)
        curr = dum 
        car = 0 
        while l1 or l2 or car :
            n1 = l1.val if l1 else 0 
            n2 = l2.val if l2 else 0 
            value = n1 + n2 + car 
            curr.next = ListNode(value%10)
            car = value//10 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
            curr= curr.next 
        return dum.next 