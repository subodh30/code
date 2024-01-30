class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        ans = 0
        for i in nums:
            if i-1 in n:
                continue
            x = i
            c=0
            while x in n:
                c+=1
                x+=1
            
            ans = max(ans, c)
        return ans