# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        cur = head = ListNode(0, None)
        hp = []
        for i, h in enumerate(lists):
            if h != None:
                heapq.heappush(hp, (h.val, i))
                lists[i] = h.next
        
        while hp:
            v, i = heapq.heappop(hp)
            cur.next = ListNode(v, None)
            if lists[i]!=None:
                heapq.heappush(hp, (lists[i].val, i))
                lists[i] = lists[i].next
            cur = cur.next
        
        return head.next
        
        
        