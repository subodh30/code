class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        d={}
        for i in range(n):
            d[i] = []
        for x,y in p:
            d[x].append(y)
            
        
        finished=[]
        vis=[]
        def isCycle(c, cs):
            nonlocal vis
            if c not in vis:
                vis.append(c)
                cs.append(c)
                for child in d[c]:
                    if child not in vis and isCycle(child, cs):
                        return True
                    elif child in cs:
                        return True
                
                cs.pop()
                return False
            
        
        for k, y in d.items():
            if k not in finished:
                if k not in vis and isCycle(k, []):
                    return False
        return True
            
        