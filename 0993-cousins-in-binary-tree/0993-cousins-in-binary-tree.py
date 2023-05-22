# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.xd = -1
        self.yd = -1
        self.xp = None
        self.yp = None
        
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
            
        self.check(root, None, 0, x, y)
        if self.xd == self.yd and self.xp != self.yp:
            return True
        return False
    
    def check(self, root, parent, d, x, y):
        if root==None:
            return
        d=d+1
        if root.val == x:
            self.xd = d
            self.xp = parent

        if root.val == y:
            self.yd = d
            self.yp = parent

        self.check(root.left, root, d, x, y)
        self.check(root.right, root, d, x, y)

            
        
        