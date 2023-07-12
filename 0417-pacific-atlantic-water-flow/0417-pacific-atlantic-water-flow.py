class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        
        ans=[]
        m, n = len(h), len(h[0])
        def rec(i, j, temp):
            nonlocal m, n, ans
            s=[]
            s.append((i, j))
            temp.add((i,j))
            vis = [[False for _ in range(n)] for _ in range(m)]
            while s:
                ii, jj = s.pop()
                if ii+1 < m and h[ii+1][jj] >= h[ii][jj] and not vis[ii+1][jj]:
                    vis[ii+1][jj]=True
                    s.append((ii+1, jj))
                    temp.add((ii+1, jj))
                if jj+1 < n and h[ii][jj+1] >= h[ii][jj] and not vis[ii][jj+1]:
                    vis[ii][jj+1]=True
                    s.append((ii, jj+1))
                    temp.add((ii, jj+1))

                if ii-1>=0 and h[ii-1][jj] >= h[ii][jj] and not vis[ii-1][jj]:
                    vis[ii-1][jj]=True
                    s.append((ii-1, jj))
                    temp.add((ii-1, jj))

                if jj-1 >= 0 and h[ii][jj-1] >= h[ii][jj] and not vis[ii][jj-1]:
                    vis[ii][jj-1]=True
                    s.append((ii, jj-1))
                    temp.add((ii, jj-1))
            return temp
                    
        
        pac=set()
        atl=set()
        for j in range(n):
            rec(0, j, pac)
        
        for i in range(m):
            rec(i, 0, pac)
        
        for j in range(n):
            rec(m-1, j, atl)
        
        for i in range(m):
            rec(i, n-1, atl)
        
        return atl.intersection(pac)
                
                
                
                