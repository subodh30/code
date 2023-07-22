class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def getAns(arr):
            if len(arr) == 1:
                return arr[0]
            dp = [0 for _ in range(len(arr))]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]
        
       
        return max(getAns(nums[:-1]), getAns(nums[1:]))