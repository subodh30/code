class Solution:
    def isValid(self, string: str) -> bool:
        s=[]
        for p in string:
            if p == ')':
                if s and s[-1] == '(':
                    s.pop()
                    continue
                else:
                    return False
            if p == "]":
                if s and s[-1] == '[':
                    s.pop()
                    continue
                else:
                    return False
            if p == "}":
                if s and s[-1] == '{':
                    s.pop()
                    continue
                else:
                    return False
            s.append(p)
        if s:
            return False
        return True
            