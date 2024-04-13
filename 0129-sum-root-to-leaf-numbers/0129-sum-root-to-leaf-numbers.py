# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def cursum(node, val):
            nonlocal ans
            if node == None:
                return
            if not node.left and not node.right:
                ans+= (10*val + node.val)
            cursum(node.left, 10*val + node.val)
            cursum(node.right, 10*val + node.val)
            return
        cursum(root, 0)
        return ans 
            
            