class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}
        e = {}
        for i, eq in enumerate(equations):
            x, y = eq
            if x not in g:
                g[x] = []
            g[x].append(y)
            e[(x,y)] = float(values[i])
            if y not in g:
                g[y] = []
            g[y].append(x)
            e[(y,x)] = float(1 / values[i])
        ans = []
        def bfs(st, ed):
            nonlocal e,g
            if st== ed:
                return float(1)
            q=[[st,1]]
            vis = set()
            vis.add(st)
            while q:
                n, val = q.pop(0)
                for y in g[n]:
                    t = val * e[(n, y)]
                    if y not in vis:
                        if y == ed:
                            return float(t)
                        q.append([y, t])
                        vis.add(y)
            return float(-1)
                    
                
            
        for x,y in queries:
            if x not in g or y not in g:
                ans.append(float(-1))
                continue
            ans.append(bfs(x,y))
        return ans