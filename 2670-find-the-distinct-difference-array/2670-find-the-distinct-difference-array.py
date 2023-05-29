class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        x=set()
        r=[]
        for i in nums[::-1]:
            x.add(i)
            r.append(len(x))
        
        r=r[::-1]
        r.append(0)
        l=[]
        ans=[]
        x=set()
        for i, n in enumerate(nums):
            x.add(n)
            l.append(len(x))
            ans.append(len(x) - r[i+1])
        return ans
            
            
            
        