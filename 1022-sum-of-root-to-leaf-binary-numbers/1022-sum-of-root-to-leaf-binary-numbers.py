# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def fill(root, arr, val):
            if root.left==None and root.right==None:
                arr.append(val + str(root.val))
            
            val = val + str(root.val)
            if root.left!=None:
                fill(root.left, arr, val)
                
            if root.right != None:
                fill(root.right, arr, val)
                
        fill(root, arr, "")
        ans = 0
        for s in arr:
            ans = ans + int(s, 2)
        
        return ans
        