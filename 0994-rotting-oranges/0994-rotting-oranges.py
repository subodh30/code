class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def bfs(i,j):
            q=[[i,j,0]]
            vis = set()
            while q:
                # print(q)
                x,y,t = q.pop(0)
                if (x,y) in vis:
                    continue
                vis.add((x,y))
                t+=1
                
                d = [[1,0], [0,1], [-1,0], [0,-1]]
                for ii, jj in d:
                    xx, yy = x+ii, y+jj
                    if xx < 0 or xx >= m or yy < 0 or yy >= n or (xx, yy) in vis:
                        continue
                    
                    if grid[xx][yy] == 2:
                        return t
                    if grid[xx][yy] == 1:
                        q.append([xx, yy, t])
            return -1
        
        ans = 0
        # return bfs(1,1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = bfs(i,j)
                    if temp == -1:
                        return -1
                    ans = max(ans, temp)
                    print("{} {} {}".format(i, j, temp))
                    
        return ans