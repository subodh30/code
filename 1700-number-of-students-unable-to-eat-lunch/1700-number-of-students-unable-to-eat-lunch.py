class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt0=0
        cnt1=0
        for i in students:
            if i==1:
                cnt1+=1
            else:
                cnt0+=1
        
        for s in sandwiches:
            if s==0 and cnt0 > 0:
                cnt0-=1
            elif s==0:
                return cnt1
            if s==1 and cnt1>0:
                cnt1-=1
            elif s==1:
                return cnt0
        return 0