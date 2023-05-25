# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        t=[]
        def find(root, t):
            if root==None:
                return 0
            l = find(root.left, t)
            r = find(root.right, t)
            t.append(abs(l-r))
            return l + r + root.val
        
        find(root, t)
        return sum(t)
            
        