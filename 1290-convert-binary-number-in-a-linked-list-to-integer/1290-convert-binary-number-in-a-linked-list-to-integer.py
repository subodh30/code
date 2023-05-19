# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bi = []
        while(head!=None):
            bi.append(head.val)
            head = head.next
            
        n = len(bi) - 1
        ans = 0
        for i,x in enumerate(bi):
            ans+=x*(2**(n-i))
            
        return ans