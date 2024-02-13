"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d={}
        def dsf(node):
            if node == None:
                return
            
            clone = None
            if node not in d:
                clone = Node(node.val)
                d[node] = clone
            clone = d[node]
            for child in node.neighbors:
                if child in d:
                    clone.neighbors.append(d[child])
                else:
                    dsf(child)
                    clone.neighbors.append(d[child])
            return clone
        
        return dsf(node)