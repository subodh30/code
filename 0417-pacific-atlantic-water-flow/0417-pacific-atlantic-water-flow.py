class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        m, n = len(h), len(h[0])
        atl, pac = set(), set()
        def dsf(i,j, visit, prevH):
            if i < 0 or i == m or j < 0 or j == n or (i,j) in visit or h[i][j] < prevH:
                return
            visit.add((i,j))
            dsf(i+1,j, visit, h[i][j])
            dsf(i-1,j, visit, h[i][j])
            dsf(i,j+1, visit, h[i][j])
            dsf(i,j-1, visit, h[i][j])
            
        for i in range(m):
            dsf(i, 0, pac, h[i][0])
            dsf(i, n-1, atl, h[i][n-1])
            
        for j in range(n):
            dsf(0, j, pac, h[0][j])
            dsf(m-1, j, atl, h[m-1][j])
        ans = []
        for i in range(m):
            for j in range(n):
                if (i,j) in atl and (i,j) in pac:
                    ans.append([i,j])
        return ans
                    