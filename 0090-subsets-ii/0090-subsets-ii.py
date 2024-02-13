class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        
        for x in nums:
            temp = set()
            for arr in ans:
                temp.add(tuple(sorted(arr.copy())))
                arr.append(x)
                temp.add(tuple(sorted(arr.copy())))
            ans = []
            for arr in temp:
                ans.append(list(arr))
        return ans