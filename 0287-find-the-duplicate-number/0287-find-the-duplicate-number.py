class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        j = nums[0]
        while n!=0:
            if nums[j]==-1:
                return j
            x = nums[j]
            nums[j] = -1
            j = x
            n-=1
        