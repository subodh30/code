class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        if n==0:
            return len(tasks)
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        
        mv = max(d.values())
        mul = (n+1) if (n+1) >= len(d.keys()) else len(d.keys())
        cnt=0
        for k, v in d.items():
            if v == mv:
                cnt+=1
        ans = (mv-1)*(n+1) + cnt
        return ans if ans > len(tasks)  else len(tasks)
        