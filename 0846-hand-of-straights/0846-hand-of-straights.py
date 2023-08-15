class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
            
        nums = sorted(hand)
        while nums:
            # print(nums)
            i = nums[0]
            g = groupSize
            while g > 0:
                if i in nums:
                    nums.remove(i)
                else:
                    return False
                g-=1
                i+=1
        return True