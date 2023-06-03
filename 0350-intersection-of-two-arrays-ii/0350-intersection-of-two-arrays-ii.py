class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            d[i] = d.get(i,0) + 1
        ans=[]
        for i in nums2:
            if d.get(i,0) != 0:
                ans.append(i)
                d[i]-=1
        return ans
        