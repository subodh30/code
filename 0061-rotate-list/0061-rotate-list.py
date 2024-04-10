# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        k = k % n
        if k == 0:
            return head
        def test(node):
            nonlocal head, k
            if node.next == None:
                node.next = head
                if k == 1:
                    return 2, node
                return 2, None
            # print(node.val)
            idx, ret = test(node.next)
            # print(idx)
            if idx == k+1:
                node.next = None
                
            if idx == k:
                return idx+1, node
            
            if idx < k:
                return idx+1, None
            
            return idx+1, ret
        
        
        return test(head)[1]
                
            
            