class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        xor = nums[0] ^ nums[1]
        for n in nums[2:]:
            xor^=n
            
        return xor