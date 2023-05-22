# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original==None:
            return original
        
        if original==target:
            return cloned
        l = self.getTargetCopy(original.left, cloned.left, target)
        if l!=None and l.val == target.val:
            return l
        return self.getTargetCopy(original.right, cloned.right, target)
        

        
        