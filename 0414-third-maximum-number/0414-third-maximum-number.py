class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fmax=-float("infinity")
        smax=-float("infinity")
        tmax=-float("infinity")
        for i in set(nums):
            if i >= fmax:
                tmax = smax
                smax = fmax
                fmax = i
                continue
            if i >= smax:
                tmax = smax
                smax = i
                continue
            if i >= tmax:
                tmax = i
        return tmax if tmax != float("-inf") else fmax
        