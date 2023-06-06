class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0, len(nums)-1
        ans=[0]*len(nums)
        for n in nums:
            if n%2==0:
                ans[i]=n
                i+=1
            else:
                ans[j] = n
                j-=1
        return ans
            
        