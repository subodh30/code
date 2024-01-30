class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for si in s:
            if si.isalpha():
                ss+=si.lower()
            elif si.isnumeric():
                ss+=si
        i=0
        while i < len(ss)//2:
            if not ss[i] == ss[len(ss) - 1 - i]:
                return False
            i+=1
        return True
            
        