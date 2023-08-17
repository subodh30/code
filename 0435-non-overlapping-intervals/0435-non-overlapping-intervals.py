class Solution:
    def eraseOverlapIntervals(self, itv: List[List[int]]) -> int:
        itv = sorted(itv)
        cnt = 0
        t = [float("-inf"), float("-inf")]
        # print(itv)
        for i in range(len(itv)):
            if t[1] <= itv[i][0]:
                t = itv[i]
                continue
            elif t[0] >= itv[i][1]:
                continue
            else:
                cnt+=1
                # print(t)
                # print(itv[i])
                # print()
                if t[1] > itv[i][1] :
                    t = itv[i]
                    
        return cnt