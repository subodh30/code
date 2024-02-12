class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def test(cur, temp):
            if temp == target:
                t = cur.copy()
                ans.add(tuple(sorted(t)))
                return
            if temp > target:
                return 
            
            for x in candidates:
                cur.append(x)
                test(cur, temp+x)
                cur.pop()
            return
        test([], 0)
        return list(ans)