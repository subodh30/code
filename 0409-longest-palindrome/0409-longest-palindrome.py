class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0) + 1
        odd=False
        ans=0
        for k,v in d.items():
            ans+=(v//2)*2
            if v%2==1:
                odd=True
        if odd:
            ans+=1
        return ans