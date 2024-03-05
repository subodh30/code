class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 2
        for i in range(2, n+1):
            x = n1+n2
            n1, n2 = n2, x
            
        return n1