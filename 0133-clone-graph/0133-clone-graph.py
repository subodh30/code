"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        d={}
        def bfs(node):
            nonlocal d
            q=[]
            q.append(node)
            if node not in d:
                d[node] = Node(node.val)
            while q:
                tnode = q.pop(0)
                for child in tnode.neighbors:
                    if child not in d:
                        d[child] = Node(child.val)
                        q.append(child)
        bfs(node)       
        for k, v in d.items():
            for child in k.neighbors:
                v.neighbors.append(d[child])
        return None if d.get(node, None) == None else d[node]
