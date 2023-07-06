class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def rec(nums, ans, arr, ss):
            nonlocal target
            
            for n in nums:
                if ss+n == target:
                    arr.append(n)
                    ans.add(tuple(sorted(arr.copy())))
                    arr.pop()
                if ss+n < target:
                    arr.append(n)
                    rec(nums, ans, arr, ss+n)
                    arr.pop()
        ans=set()
        arr=[]
        ss=0
        nums.sort()
        rec(nums, ans, arr, ss)
        return ans
        