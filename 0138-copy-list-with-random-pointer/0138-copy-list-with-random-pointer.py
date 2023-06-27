"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={}
        cur = head
        new = nhead = Node(0, None)
        while cur != None:
            node = Node(cur.val, None)
            d[cur] = node
            new.next = node
            new, cur = new.next, cur.next
        
        cur = head
        new=nhead.next
        while cur!=None:
            if cur.random == None:
                new.random = None
            else:
                new.random = d[cur.random]
            new, cur = new.next, cur.next
            
        return nhead.next
        