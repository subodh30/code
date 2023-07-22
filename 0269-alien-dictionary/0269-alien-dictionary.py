class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d={ c:set() for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            ml = min(len(w1), len(w2))
            if w1[:ml] == w2[:ml] and len(w1) > len(w2):
                return ""
            
            for j in range(ml):
                if w1[j] != w2[j]:
                    d[w1[j]].add(w2[j])
                    break
        v={}
        ans=[]
        def dfs(c):
            nonlocal d
            if c in v:
                return v[c]
            
            v[c] = True
            for child in d[c]:
                if dfs(child):
                    return True
            v[c] = False
            ans.append(c)
            return False
        
        for c in d:
            if dfs(c):
                return ""
        
        return "".join(ans[::-1])
        
