class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        cnt=0
        def rec(i, j):
            nonlocal m,n
            q=[]
            q.append((i, j))
            grid[i][j]=0
            while q:
                ii, jj = q.pop(0)
                if ii+1<m and grid[ii+1][jj]=="1":
                    grid[ii+1][jj]=0
                    q.append((ii+1, jj))
                if jj+1<n and grid[ii][jj+1]=="1":
                    grid[ii][jj+1]=0
                    q.append((ii, jj+1))
                if ii-1>=0 and grid[ii-1][jj]=="1":
                    grid[ii-1][jj]=0
                    q.append((ii-1, jj))
                if jj-1 >=0  and grid[ii][jj-1]=="1":
                    grid[ii][jj-1]=0
                    q.append((ii, jj-1))
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    cnt+=1
                    rec(i, j)
        
        return cnt