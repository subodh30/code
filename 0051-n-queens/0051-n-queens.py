class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat = [[False for _ in range(n)] for _ in range(n)]
        ans = set()
        def convert(mat):
            ret = []
            for row in mat:
                s=""
                for cell in row:
                    if cell:
                        s+="Q"
                    else:
                        s+="."
                ret.append(s)
            return tuple(ret)
            
            
            
        def find(mat, cnt, na, pa, ca):
            nonlocal ans
            if cnt == n:
                ans.add(convert(mat))
                return
            for j in range(n):
                if (not mat[cnt][j]) and (j not in ca) and((cnt+j) not in pa) and ((cnt-j) not in na):
                    mat[cnt][j] = True
                    pa.append(cnt+j)
                    na.append(cnt-j)
                    ca.append(j)
                    find(mat, cnt+1, na, pa, ca)
                    mat[cnt][j] = False
                    pa.pop()
                    ca.pop()
                    na.pop()
                        
        find(mat, 0, [], [], [])
        return ans
        