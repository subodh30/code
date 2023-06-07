class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        i,j=0,len(nums)-1
        for n in nums:
            if n%2==0:
                ans[i]=n
                i+=2
            else:
                ans[j]=n
                j-=2
        return ans
        