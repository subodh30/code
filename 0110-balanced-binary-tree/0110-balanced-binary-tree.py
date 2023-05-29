# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root==None:
                return [0, True]
            
            left, lc = check(root.left)
            right, rc = check(root.right)
            res = lc and rc
            if abs(left-right)<2 and res:
                return [max(left, right) + 1, True]
            else:
                return [max(left, right) + 1, False]
            
       
        return check(root)[1]
        
        