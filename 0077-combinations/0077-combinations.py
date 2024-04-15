class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(i, temp):
            
            if len(temp) == k:
                ans.append(temp.copy())
                return
            
            for x in range(i, n+1):
                temp.append(x)
                comb(x+1, temp)
                temp.pop()
            return
        comb(1,[])
        return ans