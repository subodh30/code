class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.insert(0, beginWord)
        d={}
        wn = len(beginWord)
        for word in wordList:
            d[word] = []
        def addNode(src, dest):
            nonlocal wn
            used = False
            for i in range(wn):
                if src[i] != dest[i]:
                    if used:
                        return False
                    else:
                        used = True
            return True
                
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                if addNode(wordList[i], wordList[j]):
                    d[wordList[i]].append(wordList[j])
                    d[wordList[j]].append(wordList[i])
        q = []
        q.append((beginWord, 0))
        vis=[]
        vis.append(beginWord)
        while q:
            word, cnt = q.pop(0)
            cnt+=1
            if word == endWord:
                return cnt
            for child in d[word]:
                if child not in vis:
                    vis.append(child)
                    q.append((child, cnt))
        
        return 0
                    
                    
            