class Solution:
    def convertToTitle(self, c: int) -> str:
        X=64
        ans=""
        while c>0:
            m = (c - 1)%26
            ans=chr(ord('A')+m) + ans
            c = (c - 1)//26
        return ans