class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        d = {}
        for n in nums:
            if d.get(n,None) == None:
                d[n] = 0
            d[n] += 1
        
        h = []
        for k, v in d.items():
            h.append((-v, k))
            
        heapq.heapify(h)
        ans = []
        i = 0
        while i < K:
            v, k = heapq.heappop(h)
            ans.append(k)
            i+=1
        return ans