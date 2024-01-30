class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        
        for i in range(1, len(nums)):
            left.append(left[-1]*nums[i-1])
            
        right = []
        right.append(1)
        nums = nums[::-1]
        for i in range(1, len(nums)):
            right.append(right[-1]*nums[i-1])
            
        right = right[::-1]
        ans=[]
        for i in range(0, len(nums)):
            ans.append(left[i]*right[i])
            
        return ans
            