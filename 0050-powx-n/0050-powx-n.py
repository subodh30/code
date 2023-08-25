class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def poww(x, n):
            if n == 0:
                return float(1)
            if x == 0:
                return float(0)
            
            ans = poww(x*x, n//2)
            return ans if n % 2==0 else ans * x
        
        ret = poww(x, abs(n))
        return ret if n > 0 else 1/ ret
        