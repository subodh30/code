class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp= [(target - i)/s for i,s in sorted(zip(position, speed))]
        
        
        cur, cnt=0,0
        for t in temp[::-1]:
            if cur < t:
                cnt+=1
                cur = t
        return cnt
                
                
        