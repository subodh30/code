class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
#         if n == 0:
#             return float(1)
        
#         if x == 0:
#             return float(0)
        
#         ans = float(1)
#         i = 0
#         while i <= abs(n):
#             ans*=x
#             i+=1
        
#         if n < 0:
#             return 1 / ans
#         return ans
        
        
#         dp = [-1 for _ in range(abs(n)+1)]
#         dp[0] = 0
#         dp[1] = x
        
#         for i in range(2,abs(n)+1):
#             dp[i] = dp[i//2] * dp[i//2]
#             if i % 2 == 1:
#                 dp[i] *= x
                
    
                
#         def poww(x, n):
#             nonlocal dp
#             # print(dp)
#             if dp[n] != -1:
#                 return dp[n]
        
#             if n%2 == 1:
#                 dp[n] = poww(x, n//2) * poww(x, n//2) * x
#                 return dp[n]
            
#             dp[n] = poww(x, n//2) * poww(x, n//2)
#             return dp[n]
        
        # if n < 0:
        #     return 1 / dp[n]
        # return dp[n]