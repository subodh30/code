class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(ans, arr):
            nonlocal nums
            if len(arr)==len(nums):
                ans.append(arr.copy())
                return
            for n in nums:
                if n not in arr:
                    arr.append(n)
                    rec(ans, arr)
                    arr.pop()
                    
        ans=[]
        rec(ans, [])
        return ans
            
        