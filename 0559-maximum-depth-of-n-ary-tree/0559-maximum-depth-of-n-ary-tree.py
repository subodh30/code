"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        dp=0
        def depth(root, d):
            nonlocal dp
            if root==None:
                return
            d= d+1
            if dp < d:
                dp = d
        
            for child in root.children:
                depth(child, d)
        depth(root,0)
        return dp
        