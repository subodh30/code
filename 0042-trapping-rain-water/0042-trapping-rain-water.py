class Solution:
    def trap(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        ans=0
        maxL, maxR = h[l], h[r]
        while l < r:
            if maxL <= maxR:
                l += 1
                a = maxL - h[l]
                if a > 0:
                    ans += a
                maxL = max(maxL, h[l])
            else:
                r -= 1
                a = maxR - h[r]
                if a > 0:
                    ans+=a
                maxR = max(maxR, h[r])
        return ans
                
                