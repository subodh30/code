class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        same=[]
        for i in nums1:
            if i in nums2:
                same.append(i)
                
        if len(same)==0:
            n1 = min(nums1)
            n2 = min(nums2)
            if n1 < n2:
                return n1*10 + n2
            else:
                return n2*10 + n1
        else:
            s = sorted(same)
            return s[0]
        