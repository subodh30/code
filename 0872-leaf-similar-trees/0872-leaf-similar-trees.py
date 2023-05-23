# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        def getLeaf(root, l):
            if root.left==None and root.right==None:
                l.append(root.val)
            
            if root.left!=None:
                getLeaf(root.left, l)
            
            if root.right!=None:
                getLeaf(root.right, l)
                
            
        getLeaf(root1, l1)
        getLeaf(root2, l2)
        return l1==l2
        