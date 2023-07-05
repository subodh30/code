class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        if n==2:
            return [[1], [1,1]]
        prev = [1,1]
        result = []
        ans = [[1], [1,1]]
        for i in range(3, n+1):
            result.append(1)
            for j in range(1, len(prev)):
                result.append(prev[j-1] + prev[j])
            result.append(1)
            ans.append(result)
            prev = result
            result=[]
        
        return ans
        