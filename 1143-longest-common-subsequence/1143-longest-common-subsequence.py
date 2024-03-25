class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    if i == 0 and j ==0:
                        dp[i][j] = 0
                    elif i ==0:
                        dp[i][j] = dp[i][j-1]
                    elif j==0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)   
        return dp[-1][-1]
                            
                            