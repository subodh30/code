class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i] = d.get(i,0) + 1
        
        for j in s:
            d[j]-=1
        
        for k,v in d.items():
            if v==1:
                return k