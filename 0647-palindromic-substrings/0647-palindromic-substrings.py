class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def check(st, ed):
            nonlocal ans
            while st>=0 and ed < len(s) and s[st] == s[ed]:
                ans+=1
                st-=1
                ed+=1
        
        for i in range(len(s)):
            check(i,i)
            check(i, i+1)
        
        return ans