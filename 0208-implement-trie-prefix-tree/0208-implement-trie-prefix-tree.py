class Trie:

    def __init__(self):
        self.d = {}
        self.end = False
        

    def insert(self, w: str) -> None:
        i = 0
        temp = self.d
        tr = None
        while i < len(w):
            if temp.get(w[i], None) == None:
                temp[w[i]] = Trie()
            tr = temp[w[i]]
            temp = tr.d
            i+=1
        tr.end = True
        
    def search(self, w: str) -> bool:
        i = 0
        temp = self.d
        tr = None
        while i < len(w):
            if temp.get(w[i], None) == None:
                return False
            tr = temp[w[i]]
            temp = tr.d
            i+=1
        if tr.end:
            return True
        return False

    def startsWith(self, p: str) -> bool:
        i = 0
        temp = self.d
        tr = None
        while i < len(p):
            if temp.get(p[i], None) == None:
                return False
            tr = temp[p[i]]
            temp = tr.d
            i+=1
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)