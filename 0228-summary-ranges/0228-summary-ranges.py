class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans =[]
        n = len(nums)
        def Add(s,e):
            nonlocal ans
            if s==e:
                ans.append(str(nums[s]))
            else:
                ans.append(str(nums[s])+"->"+str(nums[e]))
                
        i=0
        while i <= n-1:
            s = i
            j = i
            while j < n-1 and nums[j+1] - nums[j] == 1:
                j+=1
            e = j
            i = j+1
            Add(s, e)
        
        return ans