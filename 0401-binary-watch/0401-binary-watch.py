class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans=[]
        for h in range(0,12):
            for m in range(0,60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    ans.append("%d:%02d" % (h, m))
        return ans
        