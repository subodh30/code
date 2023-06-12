class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        x = math.floor(len(nums)/2)
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > x:
                return i
            
        # for k, v in d.items():
        #     if v > x:
        #         return k
        