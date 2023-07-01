# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        mxl = 0
        def findC(root, val, cnt):
            if root == None:
                return cnt
            
            if root.val == val:
                l = findC(root.left, val, cnt) + 1
                r = findC(root.right, val, cnt) + 1
                return max(l, r)
            return cnt
            
                
        def find(root):
            nonlocal mxl
            if root == None:
                return 
            
            l = findC(root.left, root.val, 0) 
            r = findC(root.right, root.val, 0) 
            
            if (l + r ) > mxl:
                mxl = l + r 
            
            find(root.left)
            find(root.right)
        
        find(root)
        return mxl
            
            
            
            
            
        