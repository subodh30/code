class Solution:
    def minMeetingRooms(self, itv: List[List[int]]) -> int:
        h = []
        for i in itv:
            heapq.heappush(h, (i[0], True))
            heapq.heappush(h, (i[1], False))
        
        ans = 1
        cnt = 0
        while h:
            time, status = heapq.heappop(h)
            
            if status:
                cnt+=1
                ans = max(ans, cnt)
            else:
                cnt-=1
                
        return ans