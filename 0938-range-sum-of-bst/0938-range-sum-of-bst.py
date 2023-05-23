# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def calc(root, low, high, ans):
            if root==None:
                return 
            if root.val >= low and root.val <= high:
                ans.append(root.val)
            calc(root.left, low, high, ans)
            calc(root.right, low, high, ans)
                
        
        calc(root, low, high, ans)
        return sum(ans)
            
            
        