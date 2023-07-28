class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        xdp = 1
        mdp = 1
        ans = max(nums)
        for i in range( len(nums)):
            if nums[i] == 0:
                xdp = 1
                mdp = 1
            else:
                xdp, mdp = max( xdp*nums[i], mdp*nums[i], nums[i]), min( xdp*nums[i], mdp*nums[i], nums[i])
                ans = max(xdp, ans)
        
#         print(xdp)
#         print(mdp)
        return ans