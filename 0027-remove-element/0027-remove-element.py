class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        i = len(nums) - 1
        j = len(nums) - 1
        while i > -1:
            if nums[i] == val:
                ans+=1
                nums[i] = nums[j]
                j-=1
            i-=1
        # print(ans)
        return len(nums) - ans