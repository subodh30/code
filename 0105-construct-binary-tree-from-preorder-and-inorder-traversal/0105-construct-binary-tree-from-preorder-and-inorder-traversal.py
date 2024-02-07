# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        value = preorder.pop(0)
        node = TreeNode(value)
        idx = inorder.index(value)
        leftArr = inorder[:max(0,idx)]
        rightArr = inorder[min(len(inorder),idx+1):]
        
        node.left = self.buildTree(preorder, leftArr)
        node.right = self.buildTree(preorder, rightArr)
        return node
        