class Solution:
    def canAttendMeetings(self, itv: List[List[int]]) -> bool:
        t=[-1, -1]
        for i in sorted(itv):
            if t[1] > i[0]:
                return False
            t = i
            
        return True