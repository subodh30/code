# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travel(i, node):
            if node== None:
                return 
            if i >= len(ans):
                ans.append(node.val)
            ans[i] = node.val
            travel(i+1, node.left)
            travel(i+1, node.right)
        travel(0, root)
        return ans