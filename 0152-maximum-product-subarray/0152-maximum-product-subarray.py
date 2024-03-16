class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1
        mn = 1
        rt = max(nums)
        for n in nums:
            if n == 0:
                mx = 1
                mn = 1
            else:
                mx, mn = max(mx * n, mn * n, n), min(mx * n, mn * n, n)
                rt = max(mx, rt)
                
        return rt