# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, cur):
            if cur == None:
                return prev
            temp = cur.next
            cur.next = prev
            return reverse(cur, temp)
        return reverse(None, head)