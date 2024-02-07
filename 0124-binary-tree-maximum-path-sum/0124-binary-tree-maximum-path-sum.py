# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def travel(node):
            nonlocal ans
            if node == None:
                return 0
            
            leftMax = travel(node.left)
            rightMax = travel(node.right)
            ans = max(ans, leftMax + rightMax + node.val, leftMax + node.val, rightMax+node.val, node.val)
            return max(leftMax+node.val, rightMax+node.val, 0)
        
        travel(root)
        return ans