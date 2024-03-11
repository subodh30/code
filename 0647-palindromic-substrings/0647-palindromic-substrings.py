class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def isPal(i,j):
            nonlocal ans
            while i > -1 and j < len(s):
                if s[i] == s[j]:
                    ans+=1
                else:
                    break
                i-=1
                j+=1
        
        for i in range(len(s)):
            isPal(i,i)
            isPal(i, i+1)
        
        return ans