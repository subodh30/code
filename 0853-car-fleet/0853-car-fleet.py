class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time= [(target - i)/s for i,s in sorted(zip(position, speed))]
        
        
        cur_car_time, cnt=0,0
        for cur_time in time[::-1]:
            if cur_car_time < cur_time:
                cnt+=1
                cur_car_time = cur_time
        return cnt
                
                
        