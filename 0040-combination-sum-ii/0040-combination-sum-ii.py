class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def rec(cds, arr, ss):
            nonlocal ans
            if ss == target:
                ans.add(tuple(arr.copy()))
                return
            if ss+sum(cds) < target:
                return
            i=0
            while i < len(cds):
                if i > 0 and cds[i-1] == cds[i]:
                    i+=1
                    continue
                if ss + cds[i] > target:
                    break
                arr.append(cds[i])
                rec(cds[i+1:], arr, ss+cds[i])
                arr.pop()
                i+=1
        ans=set()
        rec(nums, [], 0)
        
        return ans