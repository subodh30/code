# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt=0
        def findG(root, mxx):
            nonlocal cnt
            if root==None:
                return 
            if root.val >= mxx:
                cnt+=1
                mxx = root.val
            findG(root.left, mxx)
            findG(root.right, mxx)

        findG(root, root.val)
        return cnt