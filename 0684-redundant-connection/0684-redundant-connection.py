class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        n = len(e)+1
        ls = []
        for i in range(n):
            s= set()
            s.add(i)
            ls.append(s)
        
        for x,y in e:
            if y in ls[x] or x in ls[y]:
                return [x,y]
            ls[x] = ls[x].union(ls[y])
            for ele in ls[x]:
                ls[ele] = ls[x]
        
        
        
                