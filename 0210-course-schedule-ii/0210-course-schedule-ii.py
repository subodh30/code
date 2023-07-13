class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        vis=[]
        ans=[]
        d={}
        for i in range(n):
            d[i]=[]
        
        for x,y in p:
            d[x].append(y)
            
        def isCycle(i, recSt):
            nonlocal vis, ans
            if i not in vis:
                vis.append(i)
                recSt.append(i)
                for child in d[i]:
                    if child not in vis and isCycle(child, recSt):
                        return True
                    elif child in recSt:
                        return True
                ans.append(recSt.pop())
                return False
        
        for i in range(n):
            if i not in vis:
                if isCycle(i, []):
                    return []
        
        return ans
        