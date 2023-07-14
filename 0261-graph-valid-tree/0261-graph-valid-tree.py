class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        p=[]
        r=[]
        for i in range(n):
            p.append(i)
            r.append(0)
            
        
        def getPar(x):
            nonlocal p
            if x == p[x]:
                return x
            p[x] = getPar(p[x])
            return p[x]
        
        def merge(x, y):
            if getPar(x) == getPar(y):
                return False
            if r[x] < r[y]:
                p[getPar(x)] = getPar(y)
            elif r[x] > r[y]:
                p[getPar(y)] = getPar(x)
            else:
                r[y]+=1
                p[getPar(x)] = getPar(y)
            return True
            
            
        for x,y in edges:
            if merge(x, y) == False:
                return False
        
        for i in range(n):
            getPar(i)
        
        
        return len(set(p)) == 1
        