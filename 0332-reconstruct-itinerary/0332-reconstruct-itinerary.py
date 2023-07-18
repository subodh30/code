class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d={}
        degree ={}
        for src, dst in tickets:
            if d.get(src, None) == None:
                d[src]=[]
                degree[src]=[0, 0]
            
            if d.get(dst, None) == None:
                d[dst]=[]
                degree[dst]=[0, 0]
            degree[src][1] += 1 
            degree[dst][0] += 1
            d[src].append(dst)
        
        
        
        an=""
        bn=""
        for node, deg in degree.items():
            if deg[0]+1 == deg[1]:
                an = node
                continue
            if deg[0] == deg[1] + 1:
                bn = node
            
        #adding edge to create cycle
        # d[bn].append(an)
        for key, dest in d.items():
            heapq.heapify(d[key])
           
        # print(d)

        # vis=set()
        def getUnvis(v):
            # nonlocal vis
            # for dst in d[v]:
            #     if (v, dst) not in vis:
            #         vis.add((v, dst))
            #         return v, dst
            if d[v]:
                return (v, heapq.heappop(d[v]))
                
            return None
            
        f=[]
        b=[]
        cur = getUnvis("JFK")
        while cur != None:
            f.append(cur)
            cur = getUnvis(cur[1])
        
        # print(f)

        while f:
            eg = f.pop()
            b.append(eg)
            cur = getUnvis(eg[0])
            while cur != None:
                f.append(cur)
                cur = getUnvis(cur[1])
        # print(b)
        ans = ["JFK"]
        while b:
            eg = b.pop()
            ans.append(eg[1])
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        