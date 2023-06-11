class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        id0=-1
        for i,n in enumerate(nums):
            if n <=0 :
                id0=i
            else:
                break
        i=id0+1
        j=id0
        print(id0)
        while j > -1 and i < len(nums):
            if nums[j]**2 > nums[i]**2:
                ans.append(nums[i]**2)
                i+=1
            else:
                ans.append(nums[j]**2)
                j-=1
                
        while j > -1:
            ans.append(nums[j]**2)
            j-=1
            
        while i < len(nums):
            ans.append(nums[i]**2)
            i+=1
        return ans
        