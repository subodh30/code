class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in n:
                x=i
                while x in n:
                    x+=1
                    
                ans = max(ans, x-i)
        return ans