class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        while j<len(nums):
            while j < len(nums) and nums[i]==nums[j]:
                j+=1
            if j < len(nums):
                i+=1
                nums[i]=nums[j]
        return i+1
            
        