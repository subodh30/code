class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        if len(a) < len(b):
            a = "0"* (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b
            
        i = len(a) - 1
        c = 0
        while i >= 0:
            t = int(a[i]) + int(b[i]) + c
            if t == 2:
                c = 1
                ans = "0" + ans
            elif t == 3:
                c = 1
                ans = "1" + ans
            elif t == 0:
                c = 0
                ans = "0" + ans
            else:
                c = 0
                ans = "1" + ans
            i = i -1
        
        if c == 1:
            ans = "1" + ans
        return ans
        