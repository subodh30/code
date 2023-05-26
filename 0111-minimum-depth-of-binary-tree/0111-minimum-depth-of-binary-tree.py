# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minval= float("infinity")
        mincnt = float("infinity")
        def find(root, cnt):
            nonlocal minval
            nonlocal mincnt
            if root==None:
                return 1
            cnt = cnt + 1
            if root.left==None and root.right==None:
                if mincnt > cnt:
                    mincnt = cnt
                    
            find(root.left, cnt)
            find(root.right, cnt)
            return 
        
        find(root, 0)
        return 0 if mincnt==float("infinity") else mincnt
        