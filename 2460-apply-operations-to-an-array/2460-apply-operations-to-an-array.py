class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        i,j=0,0
        while j < len(nums):
            if nums[j]!=0:
                nums[i] = nums[j]
                i+=1
            j+=1
            
        while i < len(nums):
            nums[i]=0
            i+=1
        return nums
        
        