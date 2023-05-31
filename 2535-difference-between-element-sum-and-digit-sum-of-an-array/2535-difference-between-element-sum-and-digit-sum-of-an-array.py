class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = 0
        dsum = 0
        for i in nums:
            esum = esum + i
            x=i
            while x!=0:
                dsum = dsum + (x % 10)
                x = x // 10
        return abs(esum - dsum)
        