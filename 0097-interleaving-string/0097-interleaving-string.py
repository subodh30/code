class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        
        dp[-1][-1] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                        
        # print(dp)
        return dp[0][0]
#         memo = {}
#         def isValid(i,j,k):
#             if i == len(s1) and j == len(s2) and k == len(s3):
#                 return True
            
#             if i == len(s1) and j == len(s2):
#                 return False
#             if k == len(s3):
#                 return False
            
#             if (i,j,k) in memo:
#                 return memo[(i,j,k)]
#             valid = False
#             if i < len(s1) and s1[i] == s3[k]:
#                 valid = isValid(i+1, j, k+1)
            
#             if j < len(s2) and s2[j] == s3[k]:
#                 valid = valid or isValid(i, j+1, k+1)
            
#             memo[(i,j,k)] = valid
#             return valid
        
#         return isValid(0,0,0)
        
        