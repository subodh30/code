class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x == 0:
                return float(0)
            if n == 0:
                return float(1)
            ans = power(x*x, n//2)
            return ans if n%2 == 0 else ans * x
        
        poww = power(x, abs(n))
        return poww if n > 0 else 1/poww
            
        