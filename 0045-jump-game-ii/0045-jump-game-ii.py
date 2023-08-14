class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur = mx = 0
        ret = 0
        while mx < len(nums)-1:
            ans = 0
            for i in range(cur, mx+1):
                ans = max(ans, i + nums[i])
            cur = mx+1
            mx = ans
            ret+=1
        return ret
            
        
#         reach = [float("inf") for _ in range(len(nums))]
#         reach[0] = 0
#         for i in range(1, len(nums)):
                
#             j = i-1
#             while j >=0:
#                 if reach[j] != float("inf") and i-j <= 1000 and i - j <= nums[j]:
#                     reach[i] = min(reach[j]+1, reach[i])
                    
#                 j-=1
#         # print(reach)
#         return reach[len(nums)-1]

