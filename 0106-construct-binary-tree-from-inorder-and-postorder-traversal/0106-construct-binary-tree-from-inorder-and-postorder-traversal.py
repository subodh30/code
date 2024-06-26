# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        val = postorder.pop()
        node = TreeNode(val)

        idx = inorder.index(val)
        left = inorder[:max(0,idx)]
        right = inorder[min(idx+1, len(inorder)):]

        node.right = self.buildTree(right, postorder)
        node.left = self.buildTree(left, postorder)
        return node
        