class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d={}
        m=[]
        md=-1
        for i in nums:
            d[i] = d.get(i,0) + 1
            if md < d[i]:
                m=[]
                md = d[i]
            if d[i] == md:
                m.append(i)
        d={}
        for li, i in enumerate(nums):
            if i in m:
                s, e = d.get(i, [-1,-1])
                if s==-1:
                    s = li
                    e = li
                else:
                    e=li
                d[i] = [s, e]
        mm = 60000
        for v in d.values():
            l = v[1] - v[0] + 1
            if l < mm:
                mm = l
        return mm
                    
        
        
        
        
        
        