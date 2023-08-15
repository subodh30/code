class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for c in s:
            if d.get(c, None) == None:
                d[c] = 0
            d[c]+=1
            
        curCnt=0
        curChar=set()
        ans = []
        for c in s:
            curCnt += 1
            curChar.add(c)
            d[c]-=1
            part = True
            for x in curChar:
                if d[x] != 0:
                    part=False
                    break
            if part:
                ans.append(curCnt)
                curCnt = 0
                curChar = set()
                
        return ans