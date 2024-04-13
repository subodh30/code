# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(node, lvl):
            if node == None:
                return
            if len(ans) == lvl:
                ans.append([])
            ans[lvl].append(node.val)
            bfs(node.left, lvl+1)
            bfs(node.right, lvl+1)
        bfs(root, 0)
        for i, arr in enumerate(ans):
            if i%2:
                ans[i] = arr[::-1]
        return ans