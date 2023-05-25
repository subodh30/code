# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(root, sub):
            if root==None and sub==None:
                return True
            if root==None:
                return False
            if sub==None:
                return False
            
            if root.val == sub.val:
                return isEqual(root.left, sub.left) and isEqual(root.right, sub.right)
            return False
        
        
        def getNode(root, val):
            nonlocal subRoot
            if root==None:
                return False
            
            if root.val == val:
                if isEqual(root, subRoot):
                    return True
            return getNode(root.left, val) or getNode(root.right, val)
        return getNode(root,subRoot.val)
        