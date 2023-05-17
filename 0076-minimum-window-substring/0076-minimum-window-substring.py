class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def hasSub(c1, c2):
            for a,b in zip(c1, c2):
                if a > b:
                    return False
            return True
                
        if len(t) > len(s):
            return ""
        c1 = [0]*60
        c2 = [0]*60
        
        for x in t:
            c1[ord(x) - 65] = c1[ord(x) - 65] + 1
       
        l, maxL = 0, float("infinity")
        res = [-1, -1]
        for r in range(len(s)):
            c2[ord(s[r]) - 65] = c2[ord(s[r]) - 65] + 1
            while hasSub(c1, c2) and l <= r:
                c2[ord(s[l]) - 65] = c2[ord(s[l]) - 65] - 1
                if maxL > r - l + 1:
                    res = [l, r]
                    maxL = r - l + 1
                l = l+1
        return "" if maxL == float("infinity") else s[res[0]:res[1]+1]