# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        st=[]
        cur = root
        head = TreeNode(0, None, None)
        new =head
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                new.right = TreeNode(cur.val, None, None)
                new = new.right
                cur = cur.right
            
        return head.right