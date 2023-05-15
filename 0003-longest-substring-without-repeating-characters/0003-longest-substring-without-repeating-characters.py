class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setx=set()
        if len(s) < 2:
            return len(s)
        l,r = 0, 1
        ans = 0
        setx.add(s[0])
        n = len(s)
        while(r < n):
            # print(setx)
            # print(str(l) + " " + str(r))
            if s[r] not in setx:
                setx.add(s[r])
                r = r + 1
            elif s[r] in setx:
                ans = max(ans, r-l)
                while s[r] in setx:
                    setx.remove(s[l])
                    l = l + 1
                    
        return max(ans, len(setx))
            
        