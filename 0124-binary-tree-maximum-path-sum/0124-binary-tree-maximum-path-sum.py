# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")
                
        def find(root):
            nonlocal mx
            if root==None:
                return 0
            
            l = find(root.left)
            r = find(root.right)
            
            mx = max(mx, root.val + max(l, 0) + max(r, 0))
            return root.val + max(max(l, 0), max(r, 0))
            
        find(root)
        return mx
            
        