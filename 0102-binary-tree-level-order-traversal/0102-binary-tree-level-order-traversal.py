# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root==None:
            return ans
        
        def trav(root, idx):
            nonlocal ans
            if root==None:
                return
            
            if len(ans) <= idx:
                ans.append([])
            
            ans[idx].append(root.val)
            trav(root.left, idx+1)
            trav(root.right, idx+1)
        
        trav(root, 0)
        return ans
        