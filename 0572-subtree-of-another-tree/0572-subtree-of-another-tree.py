# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getNode(root, val, arr):
            if root==None:
                return
            
            if root.val == val:
                arr.append(root)
            
            lr = getNode(root.left, val, arr)
            
            rr = getNode(root.right, val, arr)
            
            
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
        
        arr = []
        getNode(root,subRoot.val, arr)
        for node in arr:
            if isEqual(node, subRoot):
                return True
        return False
        