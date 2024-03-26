class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def getComb(i, amt):
            if amt > amount or i >= len(coins):
                return 0
            if amt == amount:
                return 1
            if (i, amt) in memo:
                return memo[(i, amt)]
            tot = 0
            for j in range(i, len(coins)):
                tot += getComb(j, amt + coins[j])
                
            memo[(i, amt)] = tot
            return tot
        
        ans = getComb(0, 0)
        # print(memo)
        return ans