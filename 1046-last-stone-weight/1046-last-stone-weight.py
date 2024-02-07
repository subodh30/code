class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -stones[0]
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x-y != 0:
                heapq.heappush(stones, x-y)
        return 0
        