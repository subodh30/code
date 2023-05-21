# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def po(root, ans):
            if root==None:
                return
            ans.append(root.val)
            po(root.left, ans)
            po(root.right, ans)
        
        ans=[]
        po(root, ans)
        return ans
        