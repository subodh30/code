class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        memo={}
        def rec(i, ss):
            nonlocal ans, memo
            if i == len(nums):
                if ss == target:
                    return 1
                else:
                    return 0
            if (i, ss) in memo:
                return memo[(i, ss)]
            memo[(i, ss)] = rec(i+1, ss+nums[i]) + rec(i+1, ss-nums[i])
            return memo[(i, ss)]
        
        return rec(0, 0)