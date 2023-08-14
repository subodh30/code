class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        mx = float("-inf")
        ans = 0
        for i in nums:
            ans += i
            if ans < i:
                ans = i
            if ans > mx:
                mx = ans
            
        return mx