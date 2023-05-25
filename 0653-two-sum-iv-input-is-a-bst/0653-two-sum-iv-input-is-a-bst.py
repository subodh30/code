# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = set()
        def find(root, k):
            nonlocal d
            if root==None:
                return False
            
            if root.val in d:
                return True
            
            d.add( k - root.val)
            return find(root.left, k) or find(root.right, k)
        
        return find(root, k)