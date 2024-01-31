# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def maxDepth(root):
            return 0 if root == None else max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        hl = maxDepth(root.left)
        hr = maxDepth(root.right)
        if abs(hl-hr) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False