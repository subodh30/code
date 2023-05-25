# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr=[]
        def rec(root, l):
            nonlocal arr
            if root==None:
                return
            if len(arr) < l:
                arr.append([])
            arr[l-1].append(root.val)
            rec(root.left, l+1)
            rec(root.right, l+1)
            return
        
        rec(root, 1)
        print(arr)
        ans = []
        for a in arr:
            ans.append(round(sum(a)/len(a), 5))
        
        return ans
        