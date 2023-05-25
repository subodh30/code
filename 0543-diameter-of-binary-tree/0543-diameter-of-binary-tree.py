# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = float("-infinity")
        def depth(root):
            if root==None:
                return 0
            
            l = depth(root.left)+1
            r = depth(root.right) + 1
            return max(l,r)
        
        def dia(root):
            nonlocal m
            if root==None:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            d = l + r
            if m < d:
                m = d
            dia(root.left)
            dia(root.right)
            return
        dia(root)
        return m
        