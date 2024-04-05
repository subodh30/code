class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = {}
        for i in range(numRows):
            d[i]=""
        i = 0
        di = 0
        ad = True
        while i < len(s):
            d[di]+=s[i]
            i+=1
            if ad:
                di += 1
                if di >= numRows-1:
                    ad = False
            else:
                di -= 1
                if di <= 0:
                    ad = True
        ans = ""
        for i in range(numRows):
            ans += d[i]
        return ans