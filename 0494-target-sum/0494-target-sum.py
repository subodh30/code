class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def getWays(i, s):
            # print(str(i) + " " + str(s))
            if s == target and i == len(nums):
                # print("res")
                return 1
            
            if i >= len(nums):
                return 0
            
            if (i, s) in memo:
                return memo[(i,s)]
            
            tot = getWays(i+1, s + nums[i])
            tot += getWays(i+1, s - nums[i])
            
            memo[(i, s)] = tot
            return tot
        
        ans = getWays(0, 0)
        # print(memo)
        return ans