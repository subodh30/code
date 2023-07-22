class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        dp=[0 for _ in range(len(c) + 1)]
        dp[0] = c[0]
        dp[1] = c[1]
        c.append(0)
        for i in range(2, len(c)):
            dp[i] = min(dp[i-1], dp[i-2]) + c[i]
        
        return dp[-1]
            