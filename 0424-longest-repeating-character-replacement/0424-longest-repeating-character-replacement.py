class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        for x in set(s):
            d[x]=0
        l=0
        ans=0
        for r in range(len(s)):
            d[s[r]]+=1
            sl = r-l+1
            if sl - max(d.values()) <= k:
                ans = max(ans, sl)
            else:
                while sl-max(d.values()) > k:
                    d[s[l]] -= 1
                    l+=1
                    sl = r - l + 1
        return ans
        