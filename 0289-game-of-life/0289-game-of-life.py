class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        m,n = len(board)-1, len(board[0])-1
        for r in range(len(board)):
            for c in range(len(board[0])):
                temp = 0
                for x,y in d:
                    if r+x > m or r+x < 0 or c+y > n or c+y < 0:
                        continue
                    vals = str(board[r+x][c+y]).split("-")
                    if vals[0] == "1":
                        temp += 1
                
                if temp < 2:
                    board[r][c] = str(board[r][c]) + "-0"
                elif temp == 2:
                    board[r][c] = str(board[r][c]) + "-" + str(board[r][c])
                elif temp == 3:
                    board[r][c] = str(board[r][c]) + "-1"
                elif temp > 3:
                    board[r][c] = str(board[r][c]) + "-0"
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = int(board[r][c].split("-")[1])
                
