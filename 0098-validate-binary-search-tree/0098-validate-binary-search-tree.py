# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def travel(node, mn, mx):
            if node==None:
                return True
            if node.val > mn and node.val < mx:
                return travel(node.left, mn, node.val) and travel(node.right, node.val, mx)
            return False
        return travel(root, float("-inf"), float("inf"))
            