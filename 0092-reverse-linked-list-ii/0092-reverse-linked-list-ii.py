# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left -= 1
        right -= 1
        def reverse(prev, cur, i):
            if cur == None:
                return prev, None
            
            nxt = cur.next
            cur.next = prev
            if i == right:
                return cur, nxt
            return reverse(cur, nxt, i+1)
        
        i=0
        temp, prev = head, None
        while i < left:
            i+=1
            prev, temp = temp, temp.next
            
        n1, n2 = reverse(prev, temp, i)
        if left == 0:
            temp.next = n2
            return n1
        prev.next = n1
        temp.next = n2
        return n1 if left == 0 else head
        
            
        