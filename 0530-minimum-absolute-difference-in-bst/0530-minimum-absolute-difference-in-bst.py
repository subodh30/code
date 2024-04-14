# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        ret = float("inf")
        def inorder(node):
            nonlocal ret
            if node == None:
                return
            inorder(node.left)
            if len(ans) == 2:
                ret = min(ret, ans[1] - ans[0])
                ans.pop(0)
            ans.append(node.val)
            inorder(node.right)
            return
        inorder(root)
        if len(ans) == 2:
            ret = min(ret, ans[1] - ans[0])
        return ret
                