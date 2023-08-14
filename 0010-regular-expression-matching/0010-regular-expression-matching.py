class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if i < 0 and j < 0:
                return True
            
            if j < 0:
                return False
            
            key = (i, j)
            if p[j] == "*":
                match = i > -1 and (p[j-1]=="." or p[j-1]==s[i])
                return dfs(i, j-2) or (match and dfs(i-1, j))
            
            if i < 0:
                return False
            if p[j]=="." or p[j]==s[i]:
                return dfs(i-1, j-1)
            
            return False
        
        # dfs(len(s)-1, len(p)-1)
        # print(dp)
        return dfs(len(s)-1, len(p)-1)