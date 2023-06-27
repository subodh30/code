# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        c=0
        while l1!=None and l2!=None:
            t = l1.val + l2.val + c
            c = t//10
            cur.next = ListNode(t%10, None)
            l1, l2, cur = l1.next, l2.next, cur.next
            
        while l1!=None:
            t = l1.val + c
            c = t//10
            cur.next = ListNode(t%10, None)
            l1, cur = l1.next, cur.next
            
        while l2!=None:
            t =  l2.val + c
            c = t//10
            cur.next = ListNode(t%10, None)
            l2, cur = l2.next, cur.next
        if c==1:
            cur.next = ListNode(1, None)
        return head.next
        
        
        