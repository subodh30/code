class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i,curInterval in enumerate(intervals):
            s, e = curInterval
            if s > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif e < newInterval[0]:
                ans.append([s,e])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        
        ans.append(newInterval)
        return ans