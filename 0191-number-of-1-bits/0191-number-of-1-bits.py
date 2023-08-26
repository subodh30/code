class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
       
        while n > 1:
            if n%2:
                ans += 1
            n=n//2
        return ans +1 if n else ans
            