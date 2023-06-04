class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        r=[]
        tot=0
        for i in nums[::-1]:
            tot+=i
            r.append(tot)
        r=r[::-1]
        print(r)
        l=[]
        tot=0
        for i in nums:
            tot+=i
            l.append(tot)
       
        for i in range(0,len(nums)):
            if l[i]==r[i]:
                return i
            
        return -1
            
        