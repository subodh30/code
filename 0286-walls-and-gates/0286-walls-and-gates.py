class Solution:
    def wallsAndGates(self, r: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(r), len(r[0])
        def rec(i, j):
            nonlocal m, n
            q=[]
            q.append((i,j, 0))
            while q:
                ii, jj, cnt = q. pop(0)
                cnt+=1
                ti = ii+1
                if ti < m and r[ti][jj] != 0 and r[ti][jj]!=-1 and cnt < r[ti][jj]:
                    r[ti][jj]=cnt
                    q.append((ti, jj, cnt))
                ti = ii-1
                if ti > -1 and r[ti][jj] != 0 and r[ti][jj]!=-1 and cnt < r[ti][jj]:
                    r[ti][jj]=cnt
                    q.append((ti, jj, cnt))
                    
                tj = jj+1
                if tj < n and r[ii][tj] != 0 and r[ii][tj]!=-1 and cnt < r[ii][tj]:
                    r[ii][tj]=cnt
                    q.append((ii, tj, cnt))
                    
                tj = jj-1
                if tj > -1 and r[ii][tj] != 0 and r[ii][tj]!=-1 and cnt < r[ii][tj]:
                    r[ii][tj]=cnt
                    q.append((ii, tj, cnt))
        
        for i in range(m):
            for j in range(n):
                if r[i][j]==0:
                    rec(i, j)
        