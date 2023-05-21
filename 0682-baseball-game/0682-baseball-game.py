class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans=[]
        for op in ops:
            if op=="C" :
                ans = ans[:-1]
            elif op=="+":
                ans.append(ans[-1] + ans[-2])
            elif op=="D":
                ans.append(ans[-1]*2)
            else:
                ans.append(int(op))

        return sum(ans)
            
        