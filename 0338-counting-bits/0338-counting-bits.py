class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        while len(ans) <= n:
            temp = ans [:]
            for x in ans:
                if len(temp) == n+1:
                    return temp
                temp.append(x+1)
            ans = temp[:]
        return ans
        
        