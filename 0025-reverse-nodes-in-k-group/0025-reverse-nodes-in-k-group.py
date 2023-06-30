# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        nhead = dummy = ListNode()
        st=[]
        while cur!=None:
            t = k
            cc = cur
            while cur!=None and t!=0:
                st.append(cur.val)
                cur = cur.next
                t-=1
            
            if t==0:
                while st:
                    dummy.next = ListNode(st.pop())
                    dummy = dummy.next
            else:
                dummy.next = cc
        return nhead.next
                
                
        