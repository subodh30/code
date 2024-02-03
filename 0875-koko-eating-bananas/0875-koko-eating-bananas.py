class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def finish(k):
            hr = 0
            for x in piles:
                hr += math.ceil(x/k)
            if hr <= h:
                return True
            return False
        ans = max(piles)
        while l <= r:
            m = (l+r)//2
            if finish(m):
                ans = min(m, ans)
                r = m-1
            else:
                l = m + 1
                
        return ans