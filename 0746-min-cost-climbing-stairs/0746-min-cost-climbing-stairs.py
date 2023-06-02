class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        dp=[0]*(len(c)+1)
        c.append(0)
        dp[0]=c[0]
        dp[1]=c[1]
        for i in range(2, len(c)):
            dp[i]=c[i]+min(dp[i-1], dp[i-2])
        return dp[-1]
            