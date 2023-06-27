# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return
        slow = fast = head
        prev=None
        while slow and fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
            
        prev.next=None
        def reverse(prev, cur):
            if cur == None:
                return prev
            head = reverse(cur, cur.next)
            cur.next = prev
            return head
        
        rev = reverse(None, slow)
        
        h1, h2 = head, rev
        while h2:
            nxt = h1.next
            h1.next = h2
            h1 = h2
            h2 = nxt
            
            
            
            
            
        
            
        
        