class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        def check(k):
            nonlocal p
            nonlocal h
            ans = 0
            for x in p:
                ans += (x//k)
                if x%k != 0:
                    ans+=1
            
            if ans <= h:
                return True
            return False
        
        l,r = 1, 10**9 + 7
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
        