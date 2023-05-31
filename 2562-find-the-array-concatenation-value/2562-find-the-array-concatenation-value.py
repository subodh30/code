class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        ans =0
        while i < j:
            ans = ans + int(str(nums[i]) + str(nums[j]))
            i+=1
            j-=1
        
        if i==j:
            ans = ans + nums[i]
        
        return ans
            
        