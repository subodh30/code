class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        longest = ret  = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                longest = max(longest, i + nums[i])
            l = r+1
            r = longest
            ret+=1
        return ret
        