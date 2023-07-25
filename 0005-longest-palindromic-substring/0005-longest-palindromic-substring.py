class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        def check(st, ed):
            nonlocal ans
            while st >= 0 and ed < len(s) and s[st] == s[ed]:
                if (ed - st + 1) > len(ans):
                    ans = s[st:ed+1]
                st-=1
                ed+=1
                
        for i in range(len(s)):
            check(i,i)
            check(i, i+1)
        
        return ans