class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def test(temp):
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return
            
            for x in nums:
                if x not in temp:
                    temp.append(x)
                    test(temp)
                    temp.pop()
                  
        test([])
        return ans