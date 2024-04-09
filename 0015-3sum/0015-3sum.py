class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        ss = set()
        def findSum(idx, targetSum):
            d ={}
            temp = []
            for i, n in enumerate(nums[idx:]):
                if n in d:
                    temp.append([d[n], n])
                else:
                    d[targetSum - n] = n
            return temp
        
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            temp = findSum(i+1, -nums[i])
            for x, y in temp:
                if (n, x, y) not in ss:
                    ans.append([n, x, y])
                    ss.add((n,x,y))
        return ans
                    