# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, mn, mx):
            if node == None:
                return True
            
            if mn < node.val < mx:
                left = valid(node.left, mn, node.val)
                right = valid(node.right, node.val, mx)
                return left and right
            return False
        return valid(root, float("-inf"), float("inf"))