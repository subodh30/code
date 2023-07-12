class Solution:
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(b), len(b[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        def rec(i, j):
            q=[]
            nonlocal vis, m , n
            q.append((i,j))
            temp = set()
            temp.add((i,j))
            mark = True
            while q:
                ii, jj = q.pop(0)
                if ii+1 ==m or jj+1==n or ii-1==-1 or jj-1 == -1:
                    mark=False
                if ii+1 < m and not vis[ii+1][jj] and b[ii+1][jj]=="O":
                    vis[ii+1][jj]=True
                    temp.add((ii+1, jj))
                    q.append((ii+1, jj))
                if ii-1 >= 0 and not vis[ii-1][jj] and b[ii-1][jj]=="O":
                    vis[ii-1][jj]=True
                    temp.add((ii-1, jj))
                    q.append((ii-1, jj))
                if jj+1 < n and not vis[ii][jj+1] and b[ii][jj+1]=="O":
                    vis[ii][jj+1]=True
                    temp.add((ii, jj+1))
                    q.append((ii, jj+1))
                if jj-1 >= 0 and not vis[ii][jj-1] and b[ii][jj-1]=="O":
                    vis[ii][jj-1]=True
                    temp.add((ii, jj-1))
                    q.append((ii, jj-1))
            if mark:
                for x,y in temp:
                    b[x][y]="X"
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and b[i][j]=="O":
                    rec(i, j)
                    
            