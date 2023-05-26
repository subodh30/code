# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=set()
        def paths(root, path):
            nonlocal ans
            if root==None:
                return
            
            if path=="":
                path = str(root.val)
            else:
                path= path + "->" + str(root.val)
            
            if root.left==None and root.right==None:
                ans.add(path)
                return
                
            paths(root.left, path)
            paths(root.right, path)
            
            return
        
        paths(root, "")
        return ans