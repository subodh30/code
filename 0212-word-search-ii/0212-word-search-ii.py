class Trie:
    def __init__(self):
        self.child={}
        self.end=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def getTrie(words):
            def addWord(word, d):
                temp = d
                for c in word:
                    if c not in temp.child:
                        temp.child[c] = Trie()
                    temp = temp.child[c]
                temp.end=True
            tri = Trie()
            for word in words:
                addWord(word, tri)
            return tri
            
        tri = getTrie(words)
        m = len(board)
        n = len(board[0])
        
        def dfs(tri, i, j, ans, curWord):
            nonlocal m , n
            if tri.end:
                ans.append(curWord)
                tri.end=False
            
            if board[i][j] in tri.child:
                c = board[i][j]
                cc = curWord + board[i][j]
                board[i][j]=None
                if i > -1 and i+1 < m and j > -1 and j < n:
                    dfs(tri.child[c], i+1, j, ans, cc)
                    
                if i > -1 and i < m and j > -1 and j+1 < n:
                    dfs(tri.child[c], i, j+1, ans, cc)
                    
                if i-1 > -1 and i < m and j > -1 and j < n:
                    dfs(tri.child[c], i-1, j, ans, cc)
                    
                if i > -1 and i < m and j-1 > -1 and j < n:
                    dfs(tri.child[c], i, j-1, ans, cc)
                
                board[i][j]=c
                if tri.child[c].end:
                    ans.append(cc)
                    tri.child[c].end=False
            
                    
        ans=[]
        for i in range(m):
                for j in range(n):
                    dfs(tri, i, j, ans, "")
        return ans
            
       
