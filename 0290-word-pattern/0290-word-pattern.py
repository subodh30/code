class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        if len(set(pattern)) != len(set(ss)):
            return False
        
        if len(pattern) != len(ss):
            return False
        d = {}
        i=0
        while i<len(ss):
            if d.get(pattern[i], None) == None:
                d[pattern[i]] = ss[i]
            
            if d[pattern[i]] != ss[i]:
                return False
            i+=1
        return True