class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        tt = [[float(inf) for _ in range(n)] for _ in range(m)]
        def rec(i, j, vis):
            nonlocal m,n,tt
            q=[]
            q.append((i,j, 0))
            vis[i][j]=True
            while q:
                ii, jj, time = q.pop(0)
                tt[ii][jj] = min(tt[ii][jj], time)
                if ii+1<m and not vis[ii+1][jj] and g[ii+1][jj]==1:
                    vis[ii+1][jj]=True
                    q.append((ii+1, jj, time+1))
                    
                if ii-1>=0 and not vis[ii-1][jj] and g[ii-1][jj]==1:
                    vis[ii-1][jj]=True
                    q.append((ii-1, jj, time+1))
                
                if jj+1<n and not vis[ii][jj+1] and g[ii][jj+1]==1:
                    vis[ii][jj+1]=True
                    q.append((ii, jj+1, time+1))
                    
                if jj-1>=0 and not vis[ii][jj-1] and g[ii][jj-1]==1:
                    vis[ii][jj-1]=True
                    q.append((ii, jj-1, time+1))
                            
        
        for i in range(m):
            for j in range(n):
                if g[i][j]==2:
                    vis = [[False for _ in range(n)] for _ in range(m)]
                    rec(i,j, vis)
                    
        for i in range(m):
            for j in range(n):
                if g[i][j]==1 and tt[i][j] == float("inf"):
                    return -1
                
        mt = 0
        for i in range(m):
            for j in range(n):
                if tt[i][j] != float("inf"):
                    mt = max(mt, tt[i][j])
        return mt
        