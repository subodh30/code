class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        ans = False
        def rec(idx, i, j):
            nonlocal m, n, ans
            if idx >= len(word):
                ans = True
                return
            
            if i > -1 and i < m and j > -1 and j < n:
                if board[i][j] == word[idx]:
                    ch = board[i][j]
                    board[i][j] = 0
                    rec(idx+1, i+1, j)
                    rec(idx+1, i-1, j)
                    rec(idx+1, i, j+1)
                    rec(idx+1, i, j-1)
                    board[i][j] = ch
                    
        for i in range(m):
            for j in range(n):
                rec(0,i,j)
        return ans
                
        