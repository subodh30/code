class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for s in strs[1:]:
            check, s = ans if len(ans) <= len(s) else s, s if len(ans) <= len(s) else ans
            i=0
            while i < len(check) and check[i] == s[i]:
                i+=1
            ans = check[:i]
        return ans