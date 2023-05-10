class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right=[0]*len(nums)
        right[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        ans=[]
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        
        return ans
        