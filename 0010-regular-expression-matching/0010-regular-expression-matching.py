class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if i < 0 and j < 0:
                return True
            
            if j < 0:
                return False
            
            key = (i, j)
            if key in dp:
                return dp[key]
            if p[j] == "*":
                match = i > -1 and (p[j-1]=="." or p[j-1]==s[i])
                dp[key] =  dfs(i, j-2) or (match and dfs(i-1, j))
                return dp[key]
            
            if i < 0:
                dp[key] = False
                return dp[key]
            if p[j]=="." or p[j]==s[i]:
                dp[key] = dfs(i-1, j-1)
                return dp[key]
            
            dp[key] = False
            return dp[key]
        
        # dfs(len(s)-1, len(p)-1)
        # print(dp)
        return dfs(len(s)-1, len(p)-1)