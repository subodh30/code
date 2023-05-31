class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
            
        for k,v in d.items():
            if v%2!=0:
                return False
        return True
        