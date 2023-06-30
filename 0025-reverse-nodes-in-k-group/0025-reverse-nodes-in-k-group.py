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
                st.append(cur)
                nxt = cur.next
                cur.next = None
                cur = nxt
                t-=1
            
            if t==0:
                while st:
                    dummy.next = st.pop()
                    dummy = dummy.next
            else:
                tst = []
                while st:
                    tst.append(st.pop())
                
                while tst:
                    dummy.next = tst.pop()
                    dummy = dummy.next
        return nhead.next
                
                
        