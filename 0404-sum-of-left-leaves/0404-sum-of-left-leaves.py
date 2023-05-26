# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans =0
        def cal(root, d):
            nonlocal ans
            if root==None:
                return
            
            if root.left==None and root.right==None and d=="l":
                ans+=root.val
                
            
                
            cal(root.left, "l")
            cal(root.right, "r")
            return
    
        cal(root, "r")
        return ans