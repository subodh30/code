# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvl=[]
        def order(root, i):
            nonlocal lvl
            if root==None:
                return
            if len(lvl) <= i:
                lvl.append(root.val)
            order(root.left, i+1)
            lvl[i]=root.val
            order(root.right, i+1)
        
        order(root, 0)
        return lvl
        