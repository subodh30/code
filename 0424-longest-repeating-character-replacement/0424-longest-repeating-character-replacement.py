class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def isGood(c, k):
            return sum(c) - max(c) <= k
        
        c=[0]*26
        l,r = 0, 0
        ans = k
        while r < len(s):
            c[ord(s[r])-65] = c[ord(s[r])-65] + 1
            while not isGood(c, k):
                c[ord(s[l]) - 65] = c[ord(s[l]) - 65] - 1
                l = l +1
            ans = max(ans, r-l+1)
            r = r + 1
        return ans
        