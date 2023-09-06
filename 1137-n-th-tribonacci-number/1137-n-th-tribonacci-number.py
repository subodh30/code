class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
            
        if n < 3:
            return 1
        
        arr = [0, 1, 1]
        
        for i in range(3, n+1):
            arr.append(arr[-1] + arr[-2] + arr[-3])
            
        return arr[-1]