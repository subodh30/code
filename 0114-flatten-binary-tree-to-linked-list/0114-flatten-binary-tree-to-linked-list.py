# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        start = node = TreeNode()
        st, cur = [], root
        while st or cur:
            if cur:
                st.append(cur.right)
                left = cur.left
                cur.right, cur.left = None, None
                node.right = cur
                node = node.right
                cur = left
            else:
                cur = st.pop()
