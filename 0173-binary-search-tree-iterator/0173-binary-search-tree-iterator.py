# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node = temp = TreeNode()
        def inorder(n):
            nonlocal temp
            if n == None:
                return
            inorder(n.left)
            right = n.right
            n.left = n.right = None
            temp.right = n
            temp = temp.right
            inorder(right)
        inorder(root)
            

    def next(self) -> int:
        self.node = self.node.right
        return self.node.val
        
    def hasNext(self) -> bool:
        if self.node.right:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()