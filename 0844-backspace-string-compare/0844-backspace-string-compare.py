class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        for i in s:
            if s1 and i == "#":
                s1.pop()
            elif i=="#":
                pass
            else:
                s1.append(i)
        s2=[]
        for i in t:
            if s2 and i == "#":
                s2.pop()
            elif i=="#":
                pass
            else:
                s2.append(i)
        return s1 == s2