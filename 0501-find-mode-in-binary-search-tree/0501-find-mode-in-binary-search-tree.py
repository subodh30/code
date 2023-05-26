# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def count(root):
            nonlocal d
            if root==None:
                return
            
            d[root.val] = 1 + d.get(root.val, 0)
            count(root.right)
            count(root.left)
            return
        
        count(root)
        x = max(list(d.values()))
        ans=[]
        for k,v in d.items():
            if v==x:
                ans.append(k)
                
        return ans