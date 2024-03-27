class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            ans += num
            if ans < num:
                ans = num
            ret = max(ans, ret)
        return ret