class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        marea=0
        def rec(i, j):
            nonlocal m,n, marea
            q=[]
            q.append((i, j))
            grid[i][j]=0
            area=0
            while q:
                ii, jj = q.pop(0)
                area+=1
                if ii+1<m and grid[ii+1][jj]:
                    grid[ii+1][jj]=0
                    q.append((ii+1, jj))
                if jj+1<n and grid[ii][jj+1]:
                    grid[ii][jj+1]=0
                    q.append((ii, jj+1))
                if ii-1>=0 and grid[ii-1][jj]:
                    grid[ii-1][jj]=0
                    q.append((ii-1, jj))
                if jj-1 >=0  and grid[ii][jj-1]:
                    grid[ii][jj-1]=0
                    q.append((ii, jj-1))
            marea = max(marea, area)
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rec(i, j)
        
        return marea
        