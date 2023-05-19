# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        even=None
        while True:
            fast = fast.next
            if fast==None:
                even=False
                break
            fast = fast.next
            if fast == None:
                even=True
                break
            slow = slow.next

        
        return slow.next if even else slow
        