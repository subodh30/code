# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def func(root, ans):
            nonlocal nums
            if root == None:
                return 
            
            ans = ans*10 + root.val
            if root.left == None and root.right == None:
                nums.append(ans)
                return
            
            func(root.left, ans)
            func(root.right, ans)
           
        func(root, 0)
        # print(nums)
        return sum(nums)