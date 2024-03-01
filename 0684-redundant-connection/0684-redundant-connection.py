class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        sets = [set()]
        for i in range(1,len(e)+1):
            s = set()
            s.add(i)
            sets.append(s)
        
        for s,d in e:
            if s in sets[d]:
                return [s,d]
            sets[s] = sets[s].union(sets[d])
            for ele in sets[s]:
                sets[ele] = sets[s]
            
        
        
        
                