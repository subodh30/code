class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        long = min (1, len(nums))
        for x in snums:
            tlong = 0
            if x-1 not in snums:
                while (x + tlong) in snums:
                    tlong+=1
            long = max(long, tlong)
        return long
        