class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, lc):
            if i >= len(s) and lc ==0:
                return True
            if i >= len(s):
                return False
            
            if lc < 0:
                return False
            
            key = (i, lc)
            if key in dp:
                return dp[key]
            
            if s[i] == "(":
                dp[key] = dfs(i+1, lc+1)
                return dp[key]
            
            if s[i] == ")":
                dp[key] = dfs(i+1, lc - 1)
                return dp[key]
            
            dp[key] = dfs(i+1, lc) or dfs(i+1, lc+1) or dfs(i+1, lc-1)
            return dp[key]
        
        
        return dfs(0, 0)
            