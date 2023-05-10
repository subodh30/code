class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                idx = nums.index(target - nums[i])
                if i != idx:
                    return [i, idx]
            except:
                continue
        return []
        