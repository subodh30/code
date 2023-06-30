# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        ret = -1
        def inorder(root, k):
            nonlocal ans
            nonlocal ret
            if root==None:
                return
            inorder(root.left, k)
            ans.append(root.val)
            if len(ans)==k:
                ret = ans[-1]
            inorder(root.right, k)
            
        inorder(root, k)
        return ret
                