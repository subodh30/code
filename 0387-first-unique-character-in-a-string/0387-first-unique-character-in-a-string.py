class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        for i, n in enumerate(s):
            if d[n]==1:
                return i
        return -1