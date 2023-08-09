class Solution:
    def longestIncreasingPath(self, mtx: List[List[int]]) -> int:
        m, n = len(mtx), len(mtx[0])
        # vis = [[0 for _ in range(n)] for _ in range(m)]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            nonlocal dp, m, n
            # if i < 0 or i >= m or j < 0 or j >= n:
            #     return
            # if vis[i][j]:
            #     return
            # vis[i][j] = 1
            if dp[i][j] != 0:
                return
            dp[i][j] = 1
            if i+1 < m and mtx[i][j] < mtx[i+1][j]:
                dfs(i+1, j)
                dp[i][j] = max(dp[i][j], dp[i+1][j]+1)
            
            if i-1 > -1 and mtx[i][j] < mtx[i-1][j]:
                dfs(i-1, j)
                dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)
            
            if j + 1 < n and mtx[i][j] < mtx[i][j+1]:
                dfs(i, j+1)
                dp[i][j] = max(dp[i][j], dp[i][j+1]+1)
                
            if j -1 > -1 and mtx[i][j] < mtx[i][j-1]:
                dfs(i, j-1)
                dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    dfs(i,j)
        dfs(0,0)
        # print(dp)
        mx = 1
        for i in range(m):
            mx = max(mx, max(dp[i]))
        return mx
        
            