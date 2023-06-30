# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        ret = True
        def inorder(root):
            nonlocal ans
            nonlocal ret
            if root == None:
                return 
            inorder(root.left)
            ans.append(root.val)
            if ret and len(ans) > 1:
                if ans[-2] >= ans[-1]:
                    ret = False
                    
            inorder(root.right)
        
        inorder(root)
        return ret