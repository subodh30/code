class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        if len(s1) > len(s2):
            return False
        for x in s1:
            c1[ord(x) - 97] += 1
            
        for i in range(len(s1)):
            c2[ord(s2[i]) - 97] += 1
            
        l= 0
        for r in range(len(s1), len(s2)):
            if c1 == c2:
                return True
            c2[ord(s2[r]) - 97] += 1
            c2[ord(s2[l]) - 97] -= 1
            l += 1
        if c1 == c2:
            return True
        return False
            
            
        