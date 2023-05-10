class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sdict = {}
        for x in nums:
            if x not in sdict:
                sdict[x] = 0
            sdict[x]+=1
            
        sdict=dict(sorted(sdict.items(), key= lambda x: x[1], reverse=True))
        return list(sdict.keys())[:k]