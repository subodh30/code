class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        i, c=0,0
        for n in nums:
            if n==target:
                c+=1
            if n < target:
                i+=1
        return [x for x in range(i, i+c)]
        