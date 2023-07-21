class Solution:
    def getRow(self, i: int) -> List[int]:
        if i==0:
            return [1]
        if i==1:
            return [1,1]
        init=[1,1]
        ans=[]
        for i in range(i-1):
            ans=[]
            ans.append(1)
            for j in range(1,len(init)):
                ans.append(init[j-1]+init[j])
            ans.append(1)
            init = ans
        
        return ans
        