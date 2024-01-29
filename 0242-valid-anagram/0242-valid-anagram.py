class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for si in s:
            if d.get(si, None) == None:
                d[si] = 0
            d[si] += 1
            
        for ti in t:
            if d.get(ti, None) == None:
                return False
            if d[ti] == 0:
                return False
            d[ti] -= 1
            
        for v in d.values():
            if v != 0:
                return False
        return True
            