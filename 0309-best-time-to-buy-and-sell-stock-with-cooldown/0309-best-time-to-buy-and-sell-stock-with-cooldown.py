class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def rec(i, buy):            
#             todo =True mean Buy... False means sell
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            if buy:
                mx1 = rec(i+1, False) - prices[i]
                mx2 = rec(i+1, True)
            else:
                mx1 = rec(i+2, True) + prices[i]
                mx2 = rec(i+1, False)
            memo[(i, buy)] = max(mx1, mx2)
            return max(mx1, mx2)
        
        return rec(0, True)