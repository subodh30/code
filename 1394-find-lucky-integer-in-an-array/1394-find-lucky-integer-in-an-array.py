class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            d[i] = d.get(i,0) + 1
        
        ans = -1
        for k,v in d.items():
            if k==v:
                if ans < k:
                    ans=k
                    
        return ans