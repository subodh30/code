class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            tmp = []
            for ar in ans:
                tmp.append(ar.copy())
                ar.append(x)
                tmp.append(ar.copy())
            ans = tmp.copy()
        return ans