# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = set()
        def findP(node):
            if not node:
                return
            
            if node == p:
                s.add(node)
                return True
            if findP(node.left) or findP(node.right):
                s.add(node)
                return True
            return False
        ans = None
        findP(root)
        def findLCA(node):
            nonlocal ans
            if node == None:
                return False
            
            if node == q:
                if node in s:
                    ans = node
                return True
            
            if findLCA(node.left) or findLCA(node.right):
                if ans == None and node in s:
                    ans = node
                return True
            return False
                
        findLCA(root)
        return ans
                
                
            
        