class Solution:
    def insert(self, itv: List[List[int]], ni: List[int]) -> List[List[int]]:
        res=[]
        for i, it in enumerate(itv):
            if ni[1] < it[0]:
                res.append(ni)
                return res + itv[i:]
            elif ni[0] > it[1]:
                res.append(it)
            else:
                ni = [min(ni[0], it[0]), max(ni[1], it[1])]
        res.append(ni)
        return res
                