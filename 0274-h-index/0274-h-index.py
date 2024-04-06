class Solution:
    def hIndex(self, citations: List[int]) -> int:
        mxC, mxP = float("-inf"), float("-inf")
        arr = [0] * 1005
        for i,c in enumerate(citations):
            arr[0] += 1
            arr[c+1] -= 1
        
        cit = 0
        ans = 0
        for i, v in enumerate(arr):
            cit += v
            if i <= cit:
                ans = i
            if cit == 0:
                break
        return ans
        