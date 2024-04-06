class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i,j = 2,2
        while j < len(nums):
            if nums[j] == nums[i-1] and nums[j] == nums[i-2]:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        return i
                
            