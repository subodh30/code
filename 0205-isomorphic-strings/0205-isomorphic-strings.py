class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        ds={}
        dt={}
        for i in range(n):
            if ds.get(s[i], None) == None:
                ds[s[i]] = t[i]
            if dt.get(t[i], None) == None:
                dt[t[i]] = s[i]
            if ds[s[i]] != t[i] or dt[t[i]] != s[i]:
                return False
        
        return True
        