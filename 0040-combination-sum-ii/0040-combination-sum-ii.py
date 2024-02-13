class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        ans = set()
        c.sort()
        def test(i, temp):
            if sum(temp) == target:
                ans.add(tuple(sorted(temp.copy())))
                return
            if i >= len(c) or sum(temp) > target:
                return
            
            for xi in range(i, len(c)):
                if xi > i and c[xi-1] == c[xi]:
                    continue
                temp.append(c[xi])
                test(xi+1, temp)
                temp.pop()
                            
        test(0, [])
        return list(ans)