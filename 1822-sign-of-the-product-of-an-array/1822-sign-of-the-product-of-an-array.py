class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nc=0
        for i in nums:
            if i==0:
                return 0
            if i < 0:
                nc+=1
                
        return 1 if nc%2==0 else -1
        
        