class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        mx = -1
        for a in arr[::-1]:
            ans.append(mx)
            mx = max(mx, a)
        
        return ans[::-1]