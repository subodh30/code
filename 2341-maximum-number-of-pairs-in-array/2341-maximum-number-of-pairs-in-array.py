class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        p=0
        l=0
        for k,v in d.items():
            if v%2!=0:
                l+=1
            p+=(v//2)
        return [p,l]
        