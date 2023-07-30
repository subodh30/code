class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        tot = sum(nums)
        if tot % 2:
            return False
        midSum = tot // 2
        v=set()
        v.add(0)
        for n in nums:
            nv = set()
            for t in v:
                if t+n==midSum:
                    return True
                nv.add(t+n)
                nv.add(t)
            v = nv
        return False