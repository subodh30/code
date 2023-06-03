class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(s):
            i,j=0,len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        for s in words:
            if isPal(s):
                return s
        return ""