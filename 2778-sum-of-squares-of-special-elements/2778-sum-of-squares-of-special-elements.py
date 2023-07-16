class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        ln = len(nums)
        for i in range(1, ln+1):
            if ln%i == 0:
                ans += nums[i-1]*nums[i-1]
        return ans
        