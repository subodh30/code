# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(prev, cur):
            nonlocal n
            if cur==None:
                return 0, False
            nxt = cur.next
            ret, isHead = remove(cur, cur.next)
            ret += 1
            if n == ret:
                if prev != None:
                    prev.next = nxt
                else:
                    return ret, True
                    
            return ret, isHead
        
        _, isHead = remove(None, head)
        if isHead:
            return head.next
        return head
        