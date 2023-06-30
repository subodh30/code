# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def get(preorder, inorder):
            if len(preorder) == 0:
                return None
            si  = -1
            for i, x in enumerate(inorder):
                if x == preorder[0]:
                    si = i
                    break
            if si == -1:
                return None
            node = TreeNode(preorder.pop(0), None, None)
            node.left = get(preorder, inorder[:si])
            node.right = get(preorder, inorder[si:])
            return node
        return get(preorder, inorder)
        
        
        