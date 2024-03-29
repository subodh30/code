class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        cur = [intervals[0][0], intervals[0][1]]
        ans = 0
        # print(intervals)
        for s,e in intervals[1:]:
            if cur[1] <= s:
                cur = [s,e]
                continue
            else:
                ans += 1
                cur = [s,min(e, cur[1])]
        return ans