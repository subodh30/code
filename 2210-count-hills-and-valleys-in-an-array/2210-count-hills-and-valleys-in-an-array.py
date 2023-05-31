class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        c=[]
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                c.append(nums[i-1])
        if c and c[-1] != nums[-1]:
            c.append(nums[-1])
        # print(c)
        ans=0
        for i in range(1, len(c)-1):
            if (c[i-1] > c[i] and c[i+1] > c[i]) or (c[i-1] < c[i] and c[i+1] < c[i]):
                ans+=1
        return ans