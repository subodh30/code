class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ins=False
        dec=False
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                ins=True
            elif nums[i-1]>nums[i]:
                dec=True
        if ins and dec:
            return False
        return True
        