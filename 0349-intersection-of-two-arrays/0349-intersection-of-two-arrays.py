class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)
        ans=[]
        for j in set(nums2):
            if j in s:
                ans.append(j)
        return ans
                