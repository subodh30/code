# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, st, cur = [], [], root
        while st or cur:
            while cur:
                if cur.right:
                    st.append(cur.right)
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            if cur and st and st[-1] == cur.right:
                right = st.pop()
                st.append(cur)
                cur = right
            else:
                ans.append(cur.val)
                cur = None
        return ans
                