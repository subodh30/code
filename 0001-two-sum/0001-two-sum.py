class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        d = {}
        for i, n in enumerate(nums):
            if n in s:
                return [d[n], i]
            diff = target - n
            s.add(diff)
            d[diff] = i
            