class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid)-1, len(grid[0])-1
        ans = 0
        def iterate(i,j):
            nonlocal ans
            q = [[i,j]]
            d = [[0,1], [0,-1], [1,0], [-1,0]]
            area = 0
            while q:
                # print(q)
                x, y = q.pop(0)
                if grid[x][y] == 1:
                    area+=1
                    grid[x][y] = 0
                    for ii, jj in d:
                        xx, yy = x+ii, y+jj
                        if not (xx<0 or xx >m or yy <0 or yy > n):
                            if grid[xx][yy] == 1:
                                q.append([xx, yy])
            ans = max(ans, area)
        
        for i in range(m+1):
            for j in range(n+1):
                if grid[i][j] == 1:
                    iterate(i,j)
        # print(grid)
        return ans