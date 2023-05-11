class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkColumn(board: List[List[str]]) -> bool:
            for i in range(9):
                sdict = {}
                for j in range(9):
                    if board[j][i] != ".":
                        if sdict.get(board[j][i]) == None:
                            sdict[board[j][i]] = 1
                        else:
                            return False
            return True
        
        def checkRow(board: List[List[str]]) -> bool:
            for i in range(9):
                sdict = {}
                for j in range(9):
                    if board[i][j] != ".":
                        if sdict.get(board[i][j]) == None:
                            sdict[board[i][j]] = 1
                        else:
                            return False
            return True
        
        def checkBox(board: List[List[str]]) -> bool:
            for i in range(3):
                for j in range(3):
                    sdict={}
                    for k in range(3):
                        for l in range(3):
                            x = i*3 + k
                            y = j*3 + l
                            if board[x][y] != ".":
                                if sdict.get(board[x][y]) == None:
                                    sdict[board[x][y]] = 1
                                else:
                                    return False
            return True
       

        return checkColumn(board) and checkRow(board) and checkBox(board)
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                