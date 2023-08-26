class Solution:
    def reverseBits(self, n: int) -> int:
        ans = [0 for _ in range(32)]
        i = 0
        while n > 1:
            ans[i] = n%2
            n=n//2
            i+=1
        if n:
            ans[i] = 1
        
        # print(ans)
        i = 1
        ret = 0
        for bit in ans[::-1]:
            ret += bit * i
            i *= 2
        
        return ret