class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d={}
        for i in range(0, len(nums)-1):
            if nums[i]==key:
                d[nums[i+1]] = 1 + d.get(nums[i+1], 0)
        
        ki,vi=-1,-1
        for k,v in d.items():
            if vi < v:
                ki=k
                vi=v
        return ki
        