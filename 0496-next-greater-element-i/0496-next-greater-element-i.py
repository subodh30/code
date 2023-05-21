class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans={}
        n = nums2[::-1]
        st.append(n[0])
        ans[n[0]] = -1
        for x in n[1:]:
            while st and st[-1] < x:
                st.pop()
            if st:
                ans[x] = st[-1]
            else:
                ans[x] = -1
            st.append(x)
        
        ret=[]
        for x in nums1:
            ret.append(ans[x])
        
        return ret