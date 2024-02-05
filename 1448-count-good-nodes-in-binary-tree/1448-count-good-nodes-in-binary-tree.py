# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def travel(mx, node):
            nonlocal ans
            if node == None:
                return
            if node.val >= mx:
                ans+=1
            travel(max(mx,node.val), node.left)
            travel(max(mx,node.val), node.right)
            
        travel(float("-inf"), root)
        return ans