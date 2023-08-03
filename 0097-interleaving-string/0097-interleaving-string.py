class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp={}
        def rec(i, j, k):
            nonlocal dp
            # print(str(i) + " " +str(j) + " " + str(k))
            if k >= len(s3):
                return True
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if i < len(s1) and j < len(s2) and k < len(s3):
                if s1[i] == s3[k] and s2[j] == s3[k]:
                    dp[(i, j, k)] = rec(i+1, j, k+1) or rec(i, j+1, k+1)
                    return dp[(i, j, k)]
                elif s1[i] == s3[k]:
                    dp[(i, j, k)] = rec(i+1, j, k+1)
                    return dp[(i, j, k)]
                elif s2[j] == s3[k]:
                    dp[(i, j, k)] = rec(i, j+1, k+1)
                    return dp[(i, j, k)]
                else:
                    dp[(i, j, k)] = False
                    return dp[(i, j, k)]
            elif i < len(s1) and k < len(s3):
                if s1[i] == s3[k]:
                    dp[(i, j, k)] = rec(i+1, j, k+1)
                    return dp[(i, j, k)]
                else:
                    dp[(i, j, k)] = False
                    return dp[(i, j, k)]
            elif j < len(s2) and k < len(s3):
                if s2[j] == s3[k]:
                    dp[(i, j, k)] = rec(i, j+1, k+1)
                    return dp[(i, j, k)]
                else:
                    dp[(i, j, k)] = False
                    return dp[(i, j, k)]
            else: 
                dp[(i, j, k)] = False
                return dp[(i, j, k)]
        return rec(0, 0 ,0)
                
        