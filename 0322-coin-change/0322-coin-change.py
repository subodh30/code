class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp=[float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                if i > coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # print(dp)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]