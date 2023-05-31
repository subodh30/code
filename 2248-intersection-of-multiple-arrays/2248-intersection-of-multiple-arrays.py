class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c=[0]*1005
        for l in nums:
            for i in l:
                c[i]+=1
        
        n = len(nums)
        ans=[]
        for i in range(0,1005):
            if c[i]==n:
                ans.append(i)
                
        return ans
        