class Solution:
    def isHappy(self, n: int) -> bool:
        def getSumOfSq(x):
            temp = 0
            for s in x:
                temp += int(s)**2
            return str(temp)
        ans=getSumOfSq(str(n))
        while len(ans) > 1:
            ans = getSumOfSq(ans)
            
        return ans == "1" or ans == "7"