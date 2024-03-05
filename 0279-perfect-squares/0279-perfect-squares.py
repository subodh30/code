class Solution:
    def numSquares(self, n: int) -> int:
        sq = []
        temp = 1
        while temp*temp <= n:
            sq.append(temp**2)
            temp+=1
        sq = sq[::-1]
        dp = [float(inf) for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            for s in sq:
                if i - s >= 0:
                    dp[i] = min(dp[i], dp[i-s]+1)
                    
        
#         def find(xx, c):
#             if xx == 0:
#                 dp[n] = min(dp[n], c)
#                 return c
#             if xx < 0:
#                 return -1
#             if xx in dp:
#                 return dp[xx]
#             dp[xx] = float("inf")
#             for s in sq:
#                 cnt = find(xx-s, c+1)
#                 if cnt != -1:
#                     dp[xx] = min(dp[xx], cnt)
#             return dp[xx]
        
#         find(n,0)
        # print(dp)
        return dp[n]
