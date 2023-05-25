# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def cr(root, s):
            if root==None:
                return ""
            
            l = cr(root.left, s)
            r = cr(root.right, s)
            s =  str(root.val) 
            if l!="" or (l=="" and r!=""):
                s =s+"(" + l + ")"
                
            if r!="":
                s = s  + "(" + r + ")"
            return s
        s = cr(root, "")
        return s
        
        
        