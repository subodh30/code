class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        n = len(nums)
        for i in range(n):
            if d.get(nums[i], None) == None:
                d[nums[i]] = i
            elif i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False