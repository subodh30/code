class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums) - 1
        tot = nums[i] + nums[j]
        while tot != target:
            if tot < target:
                i = i+1
            else:
                j = j-1
            tot = nums[i] + nums[j]
        return [i+1, j+1]
        