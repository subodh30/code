class WordDictionary:

    def __init__(self):
        self.d={}

    def addWord(self, word: str) -> None:
        tmp = self.d
        for w in word:
            if w not in tmp:
                tmp[w]={}
            tmp = tmp[w]
        if "end" not in tmp:
            tmp["end"] = ""
    
    def search(self, word: str) -> bool:
        def find(word, t):
            for i, w in enumerate(word):
                if w == ".":
                    for letter in t:
                        if "end" != letter and find(word[i+1:], t[letter]):
                            return True
                    return False
                else:
                    if w not in t:
                        return False
                    t = t[w]
            if "end" in t:
                return True
            return False
        
        return find(word, self.d)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)