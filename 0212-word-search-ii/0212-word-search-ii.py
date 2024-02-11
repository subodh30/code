class Solution:
    def findWords(self, b: List[List[str]], words: List[str]) -> List[str]:
        t = {}
        m,n = len(b)-1, len(b[0])-1
        for word in words:
            tmp = t
            for w in word:
                if w not in tmp:
                    tmp[w] = {}
                tmp = tmp[w]
            if "end" not in tmp:
                tmp["end"]=""
        
        # print(t)
        d = [(1,0), (0, 1), (-1, 0), (0, -1)]
        ans = set()
        vis = set()
        def dsf(i,j, tmp, word, vis):
            # print(word)
            nonlocal ans
            if "end" in tmp:
                ans.add(word)
            if i < 0 or i > m or j < 0 or j > n or (i,j) in vis:
                return
            # print(b[i][j])
            if b[i][j] in tmp:
                tmp = tmp[b[i][j]]
                word+=b[i][j]
                if "end" in tmp:
                    ans.add(word)
                vis.add((i, j))  
                for x,y in d:
                    ni, nj = i+x, j+y
                    # print(str(ni) + " " + str(nj))
                    dsf(ni,nj, tmp, word, vis)
                vis.remove((i,j))
            return
        
        for i in range(m+1):
            for j in range(n+1):
                vis = set()
                dsf(i,j, t, "", vis)
        # dsf(2,3, t, "", vis)
        return ans
                    
            
        