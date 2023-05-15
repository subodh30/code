class Solution:
    def maxProfit(self, p: List[int]) -> int:
        minV = p[0]
        ans = 0
        for a in p:
            if a < minV:
                minV = a
            ans = max(ans, a - minV)
        return ans
        