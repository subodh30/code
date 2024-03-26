class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)) ]
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for ci in range(len(coins)):
            for amt in range(1, amount+1):
                if amt - coins[ci] >= 0:
                    dp[ci][amt] = dp[ci][amt - coins[ci]]
                if ci > 0:
                    dp[ci][amt] += dp[ci-1][amt]
                
        # print(dp)
        return dp[-1][-1]
    
        
#         memo = {}
#         def getComb(i, amt):
#             if amt > amount or i >= len(coins):
#                 return 0
#             if amt == amount:
#                 return 1
#             if (i, amt) in memo:
#                 return memo[(i, amt)]
#             tot = 0
#             for j in range(i, len(coins)):
#                 tot += getComb(j, amt + coins[j])
                
#             memo[(i, amt)] = tot
#             return tot
        
#         ans = getComb(0, 0)
#         # print(memo)
#         return ans