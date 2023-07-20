class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h=[]
        n = len(grid)
        heapq.heappush(h, (grid[0][0], 0, 0))
        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vis=set()
        while h:
            val, i, j = heapq.heappop(h)
            vis.add((i, j))
            if i==n-1 and j==n-1:
                return val
            for x, y in dr:
                ii = x+i
                jj = y+j
                if ii < 0 or jj < 0 or ii >= n or jj >= n:
                    continue
                if (ii, jj) in vis:
                    continue
                vis.add((ii, jj))
                heapq.heappush(h, (max(val, grid[ii][jj]), ii, jj))
        
        
        
        
        
        
        
#         n = len(grid)
#         i, j = max(grid[0][0], grid[n-1][n-1]), n*n - 1
#         ans = i
#         vis = set()
#         def dfs(i, j, val):
#             nonlocal vis, n
#             vis.add((i,j))
#             if i==0 and j==0:
#                 return True
            
#             ans = False
#             if grid[i][j] <= val:
#                 if  i+1 < n and (i+1, j) not in vis:
#                     ans= ans or dfs(i+1, j, val)
#                 if  i-1 >= 0 and (i-1, j) not in vis:
#                     ans = ans or dfs(i-1, j, val)
#                 if j+1 < n and (i, j+1) not in vis:
#                     ans = ans or dfs(i, j+1, val)
#                 if j-1 >= 0 and (i, j-1) not in vis:
#                     ans = ans or dfs(i, j-1, val)
#                 return ans
#             else:
#                 return False
            
            
            
#         def check(val):
#             nonlocal vis
#             vis = set()
#             return dfs(n-1, n-1, val)
            
#         while i <= j:
#             mid = (i+j)//2
#             if check(mid):
#                 ans = mid
#                 j = mid - 1
#             else:
#                 i = mid + 1
#         return ans