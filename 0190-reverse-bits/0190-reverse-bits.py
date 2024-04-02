class Solution:
    def reverseBits(self, n: int) -> int:
        t = []
        while n > 0:
            t.append(n%2)
            n = n // 2
        while len(t) < 32:
            t.append(0)
        ans = 0
        p = 0
        for x in t[::-1]:
            ans += (x * 2**p)
            p+=1
        return ans
            
        