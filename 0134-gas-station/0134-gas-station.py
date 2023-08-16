class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tot=0
        i=0
        for ii in range(len(gas)):
            tot+=(gas[ii] - cost[ii])
            if tot<0:
                tot=0
                i=ii+1
                
        return i