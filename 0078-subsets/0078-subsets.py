class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(prev, idx):
            if idx >= len(nums):
                return prev
            
            ans = []
            for arr in prev:
                ans.append(arr.copy())
                arr.append(nums[idx])
                ans.append(arr)
            return rec(ans, idx+1)
        
        return rec([[]], 0)
                
            
            
        