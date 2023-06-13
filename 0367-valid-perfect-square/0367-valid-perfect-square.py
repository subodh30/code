class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        l,r = 0, n//2+1
        while l <= r:
            mid = (l+r)//2
            if mid * mid == n:
                return True
            if mid*mid < n:
                l = mid + 1
            else:
                r = mid - 1
            
        if l*l == n or r*r == n:
            return True
        return False
        
        