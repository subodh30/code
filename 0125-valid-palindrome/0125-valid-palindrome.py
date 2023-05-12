class Solution:
    def isPalindrome(self, s: str) -> bool:
        def loop(a):
            return a.isalpha() or a.isdigit()
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i<j and not loop(s[i]):
                i=i+1
            while j > i and not loop(s[j]):
                j=j-1
            # print(str(i) + " " + str(j))
            if s[i] != s[j]:
                return False
            i=i+1
            j=j-1
        return True