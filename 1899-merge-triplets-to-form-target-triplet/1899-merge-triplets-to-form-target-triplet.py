class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#         if target in triplets:
#             return True
        
        
        temp = []
        for x in triplets: 
            if x[0] <= target[0] and x[1] <= target[1] and x[2] <= target[2]:
                temp.append(x)
        # print(temp)
        fi = set([x[0] for x in temp])
        se = set([x[1] for x in temp])
        th = set([x[2] for x in temp])

        if target[0] not in fi or target[1] not in se or target[2] not in th:
            return False
        
        return len(temp) > 0