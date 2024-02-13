class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        m,n = len(grid)-1, len(grid[0])-1
        ans = 0
        def iterate(i,j):
            q = [[i,j]]
            d = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                i,j = q.pop(0)
                for x,y in d:
                    xi, yj = i+x, j+y
                    if not (xi < 0 or xi > m or yj < 0 or yj > n):
                        if grid[xi][yj] == "1":
                            q.append([xi,yj])
                            grid[xi][yj] = "-"
        for i in range(m+1):
            for j in range(n+1):
                if grid[i][j] == "1":
                    ans+=1
                    iterate(i,j)
        return ans
