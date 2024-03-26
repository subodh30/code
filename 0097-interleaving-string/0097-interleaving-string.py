class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def isValid(i,j,k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if i == len(s1) and j == len(s2):
                return False
            if k == len(s3):
                return False
            
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            valid = False
            if i < len(s1) and s1[i] == s3[k]:
                valid = isValid(i+1, j, k+1)
            
            if j < len(s2) and s2[j] == s3[k]:
                valid = valid or isValid(i, j+1, k+1)
            
            memo[(i,j,k)] = valid
            return valid
        
        return isValid(0,0,0)
        
        