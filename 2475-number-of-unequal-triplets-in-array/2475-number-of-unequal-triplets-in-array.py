class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[j]!=nums[k] and nums[i] != nums[k]:
                        ans+=1
        return ans
        