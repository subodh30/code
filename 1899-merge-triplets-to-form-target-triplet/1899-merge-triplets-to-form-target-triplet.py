class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        values = [[], [], []]
        for tri in triplets:
            if tri[0] <= target[0] and tri[1] <= target[1] and tri[2] <= target[2]:
                values[0].append(tri[0])
                values[1].append(tri[1])
                values[2].append(tri[2])
                
        print(values)
        if target[0] in values[0] and target[1] in values[1] and target[2] in values[2]:
            return True
        return False