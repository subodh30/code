class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for i in range(k):
            heapq.heappush(hp, nums[i])
            
        for i in range(k, len(nums)):
            heapq.heappushpop(hp, nums[i])
        
        return heapq.heappop(hp)