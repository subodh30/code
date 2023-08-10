class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        m, n = len(w1), len(w2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m, -1, -1):
            dp[i][n] = m-i
            
        for i in range(n , -1, -1):
            dp[m][i] = n-i
            
        # print(dp)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j]+1, dp[i][j+1]+1, dp[i+1][j+1]+1)
        return dp[0][0]