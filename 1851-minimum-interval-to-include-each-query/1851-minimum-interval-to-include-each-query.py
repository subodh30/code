class Solution:
    def minInterval(self, itv: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(queries))]
        h =[]
        itv.sort()
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort()
        # print(itv)
        # print(qs)
        j = 0
        for q, i in qs:
            while j < len(itv):
                if q >= itv[j][0]:
                    heapq.heappush(h, (itv[j][1] - itv[j][0]+1, itv[j][1]))
                    j+=1
                else:
                    break
            while h and h[0][1] < q:
                heapq.heappop(h)
            # print(h)
            if len(h) != 0:
                ans[i] = h[0][0]
            
        return ans
            
