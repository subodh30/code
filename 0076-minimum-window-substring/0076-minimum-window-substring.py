class Solution:
    def minWindow(self, s: str, t: str) -> str:
        comm = set(s+t)
        dt = {}
        ds={}
        for x in comm:
            dt[x]=0
            ds[x]=0
            
        for x in t:
            dt[x]+=1
            
        def check(dt,ds):
            for x in comm:
                if dt[x] > ds[x]:
                    return False
                
            return True
        
        l=0
        ans = float("inf")
        ret = ""
        for r in range(len(s)):
            ds[s[r]]+=1
            if check(dt, ds):
                while check(dt,ds):
                    ds[s[l]]-=1
                    l+=1
                if ans > (r-l+2):
                    ans = r - l + 2
                    ret = s[max(0, l-1):min(r+1, len(s))]
        
        return "" if ans == float("inf") else ret
                