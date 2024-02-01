class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        buy = prices[0]
        for p in prices[1:]:
            buy = min(buy, p)
            pro=max(pro, p - buy)
        return pro