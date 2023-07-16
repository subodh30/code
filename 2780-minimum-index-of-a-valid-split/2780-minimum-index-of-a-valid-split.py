class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d={}
        mv = 0
        de = -1
        left=[]
        for n in nums:
            if d.get(n, None) == None:
                d[n]=0
            d[n]+=1
            if d[n] > mv:
                mv = d[n]
                de = n
            left.append((de, mv))
        
        d={}
        right=[]
        mv=0
        de=-1
        for n in nums[::-1]:
            if d.get(n, None) == None:
                d[n]=0
            d[n]+=1
            if d[n] > mv:
                mv = d[n]
                de = n
            right.append((de, mv))
        right = right[::-1]

        n = len(nums)
        for i in range(n-1):
            if left[i][0] == right[i+1][0]:
                ll = i+1
                rl = n-ll
                if left[i][1]*2 > ll and right[i+1][1]*2 > rl:
                    return i
        
        return -1
                
        
            