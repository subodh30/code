# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d ={}
        def findP(root):
            nonlocal d
            nonlocal p
            if root == None:
                return False
            if root == p:
                d[root.val] = root
                return True
            
            if findP(root.left):
                d[root.val] = root
                return True
            
            if findP(root.right):
                d[root.val] = root
                return True
            return False
        
        findP(root)
        # print(d.keys())
        def getLCA(root):
            nonlocal d
            nonlocal q
            
            if root == None:
                return None, False
            
            if root.val == q.val:
                if d.get(root.val, None) == None:
                    return None, True
                else:
                    return root, True
                
            lr, l = getLCA(root.left)
            if l and lr==None:
                 if d.get(root.val, None) == None:
                    return None, True
                 else:
                    return root, True
            elif l:
                return lr, l
                
            rr, r = getLCA(root.right)
            if r and rr==None:
                 if d.get(root.val, None) == None:
                    return None, True
                 else:
                    return root, True
            elif r:
                return rr, r
            return None, False
        
        return getLCA(root)[0]
            
                
                