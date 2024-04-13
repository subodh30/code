# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def find(node):
            nonlocal ans
            if node == None:
                return False, False
            findP, findQ = False, False
            if node == p:
                findP =True
            if node == q:
                findQ = True
            fp, fq = find(node.left)
            pf, qf = find(node.right)
            findP = findP or fp or pf
            findQ = findQ or fq or qf
            if findP and findQ and not ans:
                ans = node
            return findP, findQ
        find(root)
        return ans
        
        
                