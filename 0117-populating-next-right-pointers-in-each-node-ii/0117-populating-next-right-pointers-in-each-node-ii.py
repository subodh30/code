"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q, q1=[root], []
        cur, prev = None, None
        while q or q1:
            if q:
                cur = q.pop(0)
                if prev:
                    prev.next = cur
                if cur.left:
                    q1.append(cur.left)
                if cur.right:
                    q1.append(cur.right)
                prev = cur
                
            else:
                q = q1.copy()
                q1=[]
                prev = None
        return root
        
#         d = {}
#         def dfs(node, lvl):
#             nonlocal d
#             if not node:
#                 return 
#             if lvl not in d:
#                 d[lvl] = []
#             d[lvl].append(node)
#             dfs(node.left, lvl+1)
#             dfs(node.right, lvl+1)
        
#         dfs(root, 0)
#         for v in d.values():
#             for i, node in enumerate(v[:-1]):
#                 node.next = v[i+1]
#         return root
                