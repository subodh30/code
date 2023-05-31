class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        a1=set()
        a2=set()
        for i in nums1:
            if i not in n2:
                a1.add(i)
        
        for i in nums2:
            if i not in n1:
                a2.add(i)
                
        return [list(a1),list(a2)]