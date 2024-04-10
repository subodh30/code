class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points = sorted(points)
        end = points[0][1]
        ans = 0
        
        while points:
            px, py = points.pop(0)
            if px <= end:
                end = min(end, py)
            else:
                ans += 1
                end = py
        return ans + 1
        