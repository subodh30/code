class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        for i in arr1:
            d[i] = d.get(i,0) + 1
        i=0
        for e in arr2:
            cnt=d[e]
            while cnt!=0:
                arr1[i]=e
                i+=1
                cnt-=1
            d.pop(e)
        
        x = sorted(d.keys())
        for e in x:
            cnt=d[e]
            while cnt!=0:
                arr1[i]=e
                i+=1
                cnt-=1
        
        return arr1
            