# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        arr = []
        prev, temp, add = head, head.next, True
        ret = ans = ListNode()
        while temp:
            if temp.val == prev.val:
                add = False
            else:
                if add:
                    ret.next = prev
                    prev.next = None
                    ret = ret.next
                add = True
            prev, temp = temp, temp.next
        if add:
            ret.next = prev
            prev.next = None
            ret = ret.next
        ret.next = None
        return ans.next
