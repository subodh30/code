class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        ri = 0
        totalGas = 0
        for i, g in enumerate(gas):
            totalGas += (g - cost[i])
            if totalGas < 0:
                totalGas = 0
                ri = i+1
        return ri