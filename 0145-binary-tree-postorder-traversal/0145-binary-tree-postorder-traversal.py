# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def po(root, ans):
            if root==None:
                return
            po(root.left, ans)
            po(root.right, ans)
            ans.append(root.val)
        
        ans=[]
        po(root, ans)
        return ans