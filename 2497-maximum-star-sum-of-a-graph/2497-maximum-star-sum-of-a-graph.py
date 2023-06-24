class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        d={}
        for i in range(len(vals)):
            d[i] = []
        for e in edges:
            d[e[0]].append(vals[e[1]])
            d[e[1]].append(vals[e[0]])
        
        maxSum = float("-inf")
        for i in range(len(vals)):
            v = d[i]
            tsum = 0
            sv = sorted(v, reverse=True)
            mmax=0
            for j in range(min(len(v), k)):
                tsum+=sv[j]
                mmax=max(mmax, tsum)
            mmax+=vals[i]
            maxSum = max(maxSum, mmax)
        
        return maxSum
                
        