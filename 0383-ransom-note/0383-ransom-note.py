class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d={}
        for i in m:
            d[i] = d.get(i,0)  +1
            
        for i in r:
            if d.get(i, 0)>0:
                d[i]-=1
            else:
                return False
        return True