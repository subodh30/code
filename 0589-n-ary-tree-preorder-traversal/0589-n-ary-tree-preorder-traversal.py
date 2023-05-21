"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def po(root, ans):
            if root == None:
                return
            ans.append(root.val)
            for child in root.children:
                po(child, ans)
            
            
        ans = []
        po(root, ans)
        return ans
        