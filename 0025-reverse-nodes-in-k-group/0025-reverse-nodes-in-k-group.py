# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        st = []
        start = node = ListNode()
        temp = head
        while temp:
            if len(st) < k:
                st.append(temp)
            else:
                while st:
                    node.next = st.pop()
                    node = node.next
                st.append(temp)
            temp = temp.next
        if len(st) == k:
            while st:
                node.next = st.pop()
                node = node.next
        else:
            while st:
                node.next = st.pop(0)
                node = node.next
        node.next = None
        return start.next