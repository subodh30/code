class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        comm = s1 & s2
        n2 = n//2
        ans = 0
        os1 = s1 - s2
        os2 = s2 - s1
        ans = 0
        if len(os1) >= n2:
            ans+=n2
        else:
            ans+=len(os1)
        
        if len(os2) >= n2:
            ans+=n2
        else:
            ans+=len(os2)
        return min(n, ans+len(comm))