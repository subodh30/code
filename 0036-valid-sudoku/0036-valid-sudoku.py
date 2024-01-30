class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        rows={}
        cols={}
        mat={}
        for x in range(9):
            rows[x]=set()
            cols[x]=set()

        for i in range(3):
            for j in range(3):
                mat[(i,j)] = set()
                
        def getMat(i,j):
            x,y = -1,-1
            if i >= 0 and i <= 2:
                x = 0
            elif i >= 3 and i <= 5:
                x = 1
            else:
                x = 2
                
            if j >= 0 and j <= 2:
                y = 0
            elif j >= 3 and j <= 5:
                y = 1
            else:
                y = 2
            return (x,y)
            
        for i in range(9):
            for j in range(9):
                if b[i][j]==".":
                    continue
                
                x,y = getMat(i,j)
                if b[i][j] in rows[i] or b[i][j] in cols[j] or b[i][j] in mat[(x,y)]:
                    return False
                
                rows[i].add(b[i][j])
                cols[j].add(b[i][j])
                mat[(x,y)].add(b[i][j])
                
        return True
        