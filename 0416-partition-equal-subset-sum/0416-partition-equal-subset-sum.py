class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target = target // 2
        ans = set()
        ans.add(0)
        for n in nums:
            temp = set()
            for s in ans:
                if s+n == target:
                    return True
                if s+n < target:
                    temp.add(s+n)
            ans.update(temp)
        return False