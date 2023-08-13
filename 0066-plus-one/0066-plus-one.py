class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        ans = []
        c=1
        for i in range(len(d)-1, -1, -1):
            t = d[i]+c
            c = t // 10
            ans.append(t % 10)
            
        
        if c==1:
            ans.append(1)
        return ans[::-1]
        
            