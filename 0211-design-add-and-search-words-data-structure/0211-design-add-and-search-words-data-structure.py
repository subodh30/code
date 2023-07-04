class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, w: str) -> None:
        tri = self.d
        for char in w:
            if char not in tri:
                tri[char] = {}
            tri = tri[char]
        tri["END"] = {}
            
    def search(self, word: str) -> bool:
        def dfs(word, curr, idx):
            if idx < len(word):
                if word[idx] == ".":
                    for key in curr:
                        if dfs(word, curr[key], idx+1):
                            return True
                    return False
                if word[idx] not in curr:
                    return False
            if idx == len(word):
                if "END" in curr:
                    return True
                else:
                    return False
            curr = curr[word[idx]]
            return dfs(word, curr, idx+1)
        return dfs(word, self.d, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)