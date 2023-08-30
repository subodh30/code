class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for t in text:
            if d.get(t, None) == None:
                d[t] = 0
                
            d[t]+=1
            
        return min([d.get("b", 0), d.get("l", 0)//2, d.get("a", 0), d.get("o", 0)//2, d.get("n", 0)])