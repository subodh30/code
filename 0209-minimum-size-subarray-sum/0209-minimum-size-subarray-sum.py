class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        ans, temp = float("inf"), 0
        while j < len(nums):
            temp += nums[j]
            if temp >= target:
                while temp >= target and i <= j:
                    ans = min(ans, j-i+1)
                    temp -= nums[i]
                    i+=1
            j += 1
        while temp >= target and i <= j:
                    ans = min(ans, j-i+1)
                    temp -= nums[i]
                    i+=1
        return 0 if ans == float("inf") else ans
        