class NumMatrix:

    def __init__(self, m: List[List[int]]):
        self.pre=[]
        for r in m:
            temp = [0]
            ss=0
            for v in r:
                ss+=v
                temp.append(ss)
            self.pre.append(temp)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=[]
        for i in range(row1, row2+1):
            r = self.pre[i][col2+1] - self.pre[i][col1]
            
            ans.append(r)
       
        return sum(ans)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)