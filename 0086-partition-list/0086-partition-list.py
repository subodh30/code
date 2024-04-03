# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        n1 = ListNode()
        n2 = ListNode()
        n2.next = head
        tn1 = n1
        temp, prev  = n2.next, n2
        while temp!= None:
            if temp.val < x:
                prev.next = temp.next
                nxt = prev.next
                tn1.next = temp
                temp.next = None
                tn1 = tn1.next
                prev, temp = prev, nxt

            else:
                prev, temp = temp, temp.next
        # print(n2)
        # print(n1)
        if n1.next == None:
            return head
        h1 = n1.next
        h2 = n2.next
        t1 = h1
        while t1.next != None:
            t1 = t1.next
        t1.next = h2
       
        return h1