class Solution:
    def titleToNumber(self, c: str) -> int:
        ans=0
        for i, n in enumerate(c[::-1]):
            x = (26**i) * (ord(n)-64)
            ans+=x
        return ans
        