# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        cur = head
        while cur!=None:
            n+=1
            cur = cur.next
        
        n = n//2
        res = [0]*n
        cur = head
        i = 0
        while i<n:
            res[i] = cur.val
            i+=1
            cur = cur.next
        n-=1
        while cur!=None:
            res[n] += cur.val
            n-=1
            cur = cur.next
            
        return max(res)
            
        
        