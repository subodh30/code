class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        d = {}
        for x in set(s):
            d[x]=0
        i, j = 0, 0
        while j < len(s):
            if d[s[j]] == 0:
                d[s[j]]+=1
                ans = max(ans, j - i + 1)
                j+=1
            else:
                while d[s[j]]!=0:
                    d[s[i]]-=1
                    i+=1
        return max(ans, j-i)