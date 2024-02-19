class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vis = set()
        m,n = len(board), len(board[0])
        def bfs(i,j):
            q=[[i,j]]
            d = [[-1,0], [0, -1], [0,1], [1,0]]
            sur, area = True, set()
            while q:
                x,y = q.pop(0)
                if (x,y) in vis:
                    continue
                vis.add((x,y))
                area.add((x,y))
                for a,b in d:
                    xx, yy = x+a, y+b
                    if xx < 0 or xx == m or yy < 0 or yy == n:
                        sur = False
                        continue
                    if board[xx][yy] == "O":
                        q.append([xx, yy])
            if sur:
                for r,s in area:
                    board[r][s] = "X"

        for i in range(m):
            for j in range(n):
                # print(vis)
                if (i,j) not in vis and board[i][j] == "O":
                    bfs(i,j)
