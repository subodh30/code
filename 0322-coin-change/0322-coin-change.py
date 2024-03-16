class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range(amount+1):
                for c in coins:
                    if i >= c:
                        dp[i] = min(dp[i], dp[i-c]+1)
        return -1 if dp[amount] == float("inf") else dp[amount]