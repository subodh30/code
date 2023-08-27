class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ans=[0, 0, 0]
        for c in moves:
            if c == "L":
                ans[0]+=1
            elif c == "R":
                ans[1]+=1
            else:
                ans[2]+=1
        
        diff = abs(ans[0]-ans[1])
        return diff+ans[2]