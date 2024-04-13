class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        req = {}
        for w in words:
            req[w] = 1 + req.get(w,0)
        ans = []
        k = len(words[0])
        def check(di):
            # print(di)
            nonlocal req
            for w in words:
                if w in di and di[w] == req[w]:
                    continue
                return False
            return True
        
        def found(j):
            nonlocal k
            ansi= j
            tot = len(words) * k + j
            if tot <= len(s):
                d = {}
                while j < tot:
                    key = s[j:j+k]
                    if key in words:
                        d[key] = d.get(key,0) + 1
                    else:
                        return
                    j+=k
                if check(d):
                    ans.append(ansi)
                
            
        j = 0
        while j < len(s):
            key = s[j:min(len(s),j+k)]
            if key in words:
                found(j)
            j+=1
        return ans