class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = [False for _ in range(len(nums))]
        reach[0] = True
        for i in range(1, len(nums)):
                
            j = i-1
            while j >=0:
                if reach[j] and i - j <= nums[j]:
                    reach[i] = True
                    break
                j-=1
        # print(reach)
        return reach[len(nums)-1]