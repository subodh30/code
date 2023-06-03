class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        for i in sorted(nums)[0:len(nums):2]:
            ans+=i
            
        return ans
        