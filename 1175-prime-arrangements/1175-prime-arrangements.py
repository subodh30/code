class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def seive(n):
            p=[True]*(n+1)
            p[1]=False
            for i in range(2,n+1):
                if p[i]:
                    for j in range(2*i, n+1, i):
                        p[j]=False
                        
            return p
        
        p = seive(n)
        cnt = 0
        for i in range(2, n+1):
            if p[i]:
                cnt+=1
        
        M = 10**9 + 7
        f=1
        for i in range(1,cnt+1):
            f = f*i % M
            
        nf = 1
        for i in range(1, n-cnt+1):
            nf = nf*i %M
        
        return (f * nf)%M
            