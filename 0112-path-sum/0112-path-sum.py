# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root, ans, target):
            if root==None:
                return False
            
            if root.left==None and root.right==None and ans + root.val == target:
                return True
            
            return path(root.left, ans+root.val, target) or path(root.right, ans+root.val, target)
        
        return path(root, 0, targetSum)
            
        