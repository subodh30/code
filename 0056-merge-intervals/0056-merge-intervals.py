class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals)
        cur = [intervals[0][0], intervals[0][1]]
        for s,e in intervals[1:]:
            if cur[1] < s:
                ans.append(cur)
                cur = [s,e]
            else:
                cur = [min(s, cur[0]), max(e, cur[1])]
        ans.append(cur)
        return ans