class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        take = set()
        rej = set()
        i = 1
        while len(take) < n:
            if i not in rej:
                take.add(i)
                if target - i > 0:
                    rej.add(target - i)
            i+=1
                    
        return sum(take)