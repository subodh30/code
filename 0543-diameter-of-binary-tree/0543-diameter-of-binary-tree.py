# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if root == None:
                return 0
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        def find(root, mxx):
            if root == None:
                return 0

            ml = maxDepth(root.left) 
            mr = maxDepth(root.right)
            maxx = max(mxx, ml+mr)
            mxxl = find(root.left, maxx)
            mxxr = find(root.right, maxx)
            return max(mxxl, mxxr, maxx)
        
        if root == None:
            return 0
        return find(root, 0)
        
        