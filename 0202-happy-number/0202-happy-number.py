class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            ans = 0
            while n!=0:
                m = n %10
                n = n//10
                ans+=m*m
            if len(str(ans)) == 1:
                return ans == 1 or ans == 7
            n = ans
        