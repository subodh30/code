class Solution:
    def merge(self, itv: List[List[int]]) -> List[List[int]]:
        ret = []
        itv = sorted(itv)
        t = itv[0]
        for i in range(len(itv)):
            if t[1] < itv[i][0]:
                ret.append(t)
                t = itv[i]
            elif t[0] > itv[i][1]:
                ret.append(itv[i])
            else:
                t = [min(t[0], itv[i][0]), max(t[1], itv[i][1])]
        
        ret.append(t)
        return ret
            