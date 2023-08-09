class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0
            
            key = (i, j)
            if key in dp:
                return dp[key]
            
            if s[i] == t[j]:
                a1 = dfs(i+1, j+1)
                # a2 = dfs(i+1, 0)
                a3 = dfs(i+1, j)
                dp[key] = a1 + a3
                return dp[key]
                # return dfs(i+1, j+1) + dfs(i+1, 0) + dfs(i+1, j)
            a1 = dfs(i+1, j)
            # a2 = dfs(i+1, 0)
            dp[key] = a1
            return dp[key]
        dfs(0, 0)
        # print(dp)
        return dp[(0,0)]
            
        
        
                