class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,v in enumerate(s):
            last[v] = i
        size = end = 0
        ans = []
        for i, v in enumerate(s):
            size+=1
            end = max(end, last[v])
            if i == end:
                ans.append(size)
                size = 0
        return ans