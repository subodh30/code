class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for x in tasks:
            if x not in d:
                d[x]=0
            d[x]+=1
            
        h = []
        for k,v in d.items():
            heapq.heappush(h, -v)
        q = []
        time = 0
        while h or q:
            time+=1
            # print(h)
            # print(q)
            # print(time)
            if h:
                val = heapq.heappop(h)
                val += 1
                if val < 0:
                    q.append((time+n, val))
            while q and q[0][0] <= time:
                _, vx = q.pop(0)
                heapq.heappush(h, vx)
            
        return time
                
            