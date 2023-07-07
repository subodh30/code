class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def rec(prev, nums, idx):
            if idx >= len(nums):
                return prev
            
            ans = []
            for arr in prev:
                if arr not in ans:
                    ans.append(arr.copy())
                arr.append(nums[idx])
                if arr not in ans:
                    ans.append(arr)
            return rec(ans, nums, idx+1)
        
        return rec([[]], sorted(nums), 0)