class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        def find(x, target):
            td={}
            ans = []
            for i, n in enumerate(nums[x:], start=x):
                if n in td:
                    ans.append([td[n], i])
                td[target-n] = i
            return ans
        for i in range(len(nums)):
            if i!=0 and nums[i-1] == nums[i]:
                continue
            arr = find(i+1, -nums[i])
            for x,y in arr:
                ans.add(tuple(sorted([nums[i], nums[x], nums[y]])))
            
        return list(ans)