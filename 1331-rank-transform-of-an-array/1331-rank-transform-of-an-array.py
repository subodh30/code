class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        srtd = []
        for i, n in enumerate(arr):
            srtd.append((n, i))
        
        srtd = sorted(srtd)
        ans = [-1]*len(arr)
        print(srtd)
        idx=1
        
        for i in range(len(arr)):
            if i==0 or srtd[i][0]==srtd[i-1][0]:
                ans[srtd[i][1]]=idx
            else:
                idx+=1
                ans[srtd[i][1]]=idx
        
        return ans
            