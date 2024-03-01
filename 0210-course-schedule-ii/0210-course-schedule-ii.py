class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}
        for i in range(numCourses):
            g[i] = []
            
        for s, d in prerequisites:
            g[s].append(d)
        ans = []
        vis=set()
        def isCycle(v, st):
            nonlocal vis
            if v in st:
                return True
            if v in vis:
                return False
            vis.add(v)
            st.append(v)
            for c in g[v]:
                if isCycle(c, st):
                    return True
            st.pop()
            ans.append(v)
            return False
            
        for i in range(numCourses):
            if i not in vis and isCycle(i, []):
                return []
        return ans