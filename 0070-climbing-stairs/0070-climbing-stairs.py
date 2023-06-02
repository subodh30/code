class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*(n+1)
        if n==1 or n==0:
            return n
        if n==2:
            return 2
        arr[1]=1
        arr[2]=2
        for i in range(3, n+1):
            arr[i]=arr[i-1] + arr[i-2]
        
        return arr[n]
        