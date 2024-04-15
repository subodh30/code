class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        def rec(i, col, left, right):
            nonlocal ans
            # print("col:{}, left:{}, right:{}".format(col, left, right))
            if i == n:
                ans += 1
                return
            
            for j in range(n):
                if j in col or (i-j) in left or (i+j) in right:
                    continue
                col.add(j)
                left.add((i-j))
                right.add((i+j))
                rec(i+1, col, left, right)
                col.remove(j)
                left.remove((i-j))
                right.remove((i+j))
        rec(0, set(), set(), set())
        return ans