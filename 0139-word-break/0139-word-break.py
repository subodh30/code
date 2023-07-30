class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        vis=set()
        fail=set()
        def dfs(st):
            nonlocal vis, words, fail
            if st=="":
                return True
            
            if st in vis:
                return True
            
            if st in fail:
                return False
            
            for word in words:
                if st.startswith(word):
                    if dfs(st[len(word):]):
                        vis.add(st)
                        return True
                    else:
                        fail.add(st)
                    
            
            return False
        
        return dfs(s)