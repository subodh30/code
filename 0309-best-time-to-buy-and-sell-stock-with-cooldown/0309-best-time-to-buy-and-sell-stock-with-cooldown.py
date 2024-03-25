class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def getProfit(i, isBuy):
            nonlocal dp
            # print(str(i) + " " + str(isBuy))
            if i >= len(prices):
                return 0
            key = (i, isBuy)
            if key in dp:
                return dp[key]
            
            if isBuy:
                mx1 = getProfit(i+1, False) - prices[i]
                mx2 = getProfit(i+1, True)
            else:
                mx1 = prices[i] + getProfit(i+2, True)
                mx2 = getProfit(i+1, False)
            dp[key] = max(mx1, mx2)
            return dp[key]
        ans = getProfit(0,True)
        # print(dp)
        return ans