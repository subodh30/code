class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p)/s for p, s in sorted(zip(position, speed), reverse=True)]
        st = []
        prev = time[0]
        ans = 1
        for x in time[1:]:
            if x > prev:
                prev = x
                ans += 1
        return ans