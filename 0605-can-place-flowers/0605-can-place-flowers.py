class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if len(f) == 1:
            if f[0] == 0 and n <= 1:
                return True
            if f[0] == 1 and n == 0:
                return True
            return False
        tot = 0
        if f[0]==0 and f[1]==0:
            tot=1
            f[0]=1
        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                tot+=1
                if tot >= n:
                    return True
        
        if f[-2]==0 and f[-1]==0:
            tot+=1
            
        if tot >= n:
            return True
        return False